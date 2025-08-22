use crate::chain::pools::{MintPoolData, PumpPool, RaydiumPool};
use anyhow::{anyhow, Result};
use serde::{Deserialize, Serialize};
use solana_client::rpc_client::RpcClient;
use solana_sdk::pubkey::Pubkey;
use std::{collections::HashMap, sync::Arc, time::Instant};
use tracing::{debug, error, info, warn};

/// Token price information
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TokenPrice {
    pub mint: String,
    pub price_usd: f64,
    pub price_sol: f64,
    pub volume_24h: f64,
    pub market_cap: f64,
    pub timestamp: u64,
    pub source: String,
}

/// Price comparison for arbitrage opportunities
#[derive(Debug, Clone)]
pub struct PriceComparison {
    pub token_mint: String,
    pub dex_prices: HashMap<String, f64>, // DEX name -> price in SOL
    pub best_buy_price: f64,
    pub best_sell_price: f64,
    pub best_buy_dex: String,
    pub best_sell_dex: String,
    pub price_spread: f64,
    pub potential_profit_percent: f64,
    pub timestamp: Instant,
}

/// Market data fetcher
pub struct MarketDataFetcher {
    rpc_client: Arc<RpcClient>,
    price_cache: HashMap<String, TokenPrice>,
    cache_ttl_seconds: u64,
}

impl MarketDataFetcher {
    pub fn new(rpc_client: Arc<RpcClient>) -> Self {
        Self {
            rpc_client,
            price_cache: HashMap::new(),
            cache_ttl_seconds: 30, // 30 seconds cache
        }
    }

    /// Fetch token price from multiple sources
    pub async fn fetch_token_price(&mut self, mint: &str) -> Result<TokenPrice> {
        // Check cache first
        if let Some(cached_price) = self.price_cache.get(mint) {
            if cached_price.timestamp + self.cache_ttl_seconds > 
               std::time::SystemTime::now()
                   .duration_since(std::time::UNIX_EPOCH)
                   .unwrap()
                   .as_secs() {
                return Ok(cached_price.clone());
            }
        }

        // Try multiple price sources
        let mut price_sources = Vec::new();

        // Try Jupiter API
        if let Ok(price) = self.fetch_jupiter_price(mint).await {
            price_sources.push(price);
        }

        // Try Birdeye API
        if let Ok(price) = self.fetch_birdeye_price(mint).await {
            price_sources.push(price);
        }

        // Try CoinGecko API
        if let Ok(price) = self.fetch_coingecko_price(mint).await {
            price_sources.push(price);
        }

        if price_sources.is_empty() {
            return Err(anyhow!("Failed to fetch price from any source for mint: {}", mint));
        }

        // Use the most recent price or average of recent prices
        let best_price = self.select_best_price(price_sources);
        
        // Cache the result
        self.price_cache.insert(mint.to_string(), best_price.clone());
        
        Ok(best_price)
    }

    /// Fetch price from Jupiter API
    async fn fetch_jupiter_price(&self, mint: &str) -> Result<TokenPrice> {
        let url = format!(
            "https://price.jup.ag/v4/price?ids={}",
            mint
        );

        let response = reqwest::get(&url).await?;
        let data: serde_json::Value = response.json().await?;

        if let Some(price_data) = data.get("data").and_then(|d| d.get(mint)) {
            let price_usd = price_data
                .get("price")
                .and_then(|p| p.as_f64())
                .ok_or_else(|| anyhow!("Invalid price format"))?;

            let price_sol = price_data
                .get("price_sol")
                .and_then(|p| p.as_f64())
                .unwrap_or(price_usd / 100.0); // Rough SOL/USD conversion

            Ok(TokenPrice {
                mint: mint.to_string(),
                price_usd,
                price_sol,
                volume_24h: 0.0, // Jupiter doesn't provide volume
                market_cap: 0.0, // Jupiter doesn't provide market cap
                timestamp: std::time::SystemTime::now()
                    .duration_since(std::time::UNIX_EPOCH)
                    .unwrap()
                    .as_secs(),
                source: "jupiter".to_string(),
            })
        } else {
            Err(anyhow!("Price not found in Jupiter response"))
        }
    }

    /// Fetch price from Birdeye API
    async fn fetch_birdeye_price(&self, mint: &str) -> Result<TokenPrice> {
        let url = format!(
            "https://public-api.birdeye.so/public/price?address={}",
            mint
        );

        let client = reqwest::Client::new();
        let response = client
            .get(&url)
            .header("X-API-KEY", "YOUR_BIRDEYE_API_KEY") // You'll need to get an API key
            .send()
            .await?;

        if response.status().is_success() {
            let data: serde_json::Value = response.json().await?;
            
            if let Some(price_data) = data.get("data") {
                let price_usd = price_data
                    .get("value")
                    .and_then(|p| p.as_f64())
                    .ok_or_else(|| anyhow!("Invalid price format"))?;

                let volume_24h = price_data
                    .get("volume24h")
                    .and_then(|v| v.as_f64())
                    .unwrap_or(0.0);

                let market_cap = price_data
                    .get("marketCap")
                    .and_then(|m| m.as_f64())
                    .unwrap_or(0.0);

                Ok(TokenPrice {
                    mint: mint.to_string(),
                    price_usd,
                    price_sol: price_usd / 100.0, // Rough conversion
                    volume_24h,
                    market_cap,
                    timestamp: std::time::SystemTime::now()
                        .duration_since(std::time::UNIX_EPOCH)
                        .unwrap()
                        .as_secs(),
                    source: "birdeye".to_string(),
                })
            } else {
                Err(anyhow!("Invalid Birdeye response format"))
            }
        } else {
            Err(anyhow!("Birdeye API request failed"))
        }
    }

    /// Fetch price from CoinGecko API
    async fn fetch_coingecko_price(&self, mint: &str) -> Result<TokenPrice> {
        // Note: CoinGecko requires coin IDs, not mint addresses
        // This is a simplified implementation
        let url = format!(
            "https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd,sol&include_24hr_vol=true&include_market_cap=true",
            mint
        );

        let response = reqwest::get(&url).await?;
        let data: serde_json::Value = response.json().await?;

        if let Some(coin_data) = data.get(mint) {
            let price_usd = coin_data
                .get("usd")
                .and_then(|p| p.as_f64())
                .ok_or_else(|| anyhow!("Invalid USD price"))?;

            let price_sol = coin_data
                .get("sol")
                .and_then(|p| p.as_f64())
                .unwrap_or(price_usd / 100.0);

            let volume_24h = coin_data
                .get("usd_24h_vol")
                .and_then(|v| v.as_f64())
                .unwrap_or(0.0);

            let market_cap = coin_data
                .get("usd_market_cap")
                .and_then(|m| m.as_f64())
                .unwrap_or(0.0);

            Ok(TokenPrice {
                mint: mint.to_string(),
                price_usd,
                price_sol,
                volume_24h,
                market_cap,
                timestamp: std::time::SystemTime::now()
                    .duration_since(std::time::UNIX_EPOCH)
                    .unwrap()
                    .as_secs(),
                source: "coingecko".to_string(),
            })
        } else {
            Err(anyhow!("Coin not found in CoinGecko response"))
        }
    }

    /// Select the best price from multiple sources
    fn select_best_price(&self, prices: Vec<TokenPrice>) -> TokenPrice {
        // For now, just return the first price
        // In a real implementation, you might want to:
        // - Average the prices
        // - Weight by source reliability
        // - Filter out outliers
        prices.into_iter().next().unwrap()
    }

    /// Calculate arbitrage opportunities from pool data
    pub async fn calculate_arbitrage_opportunities(
        &self,
        pool_data: &MintPoolData,
    ) -> Result<Vec<PriceComparison>> {
        let mut opportunities = Vec::new();
        let token_mint = pool_data.mint.to_string();

        // Calculate prices from different DEX pools
        let mut dex_prices = HashMap::new();

        // Calculate Raydium prices
        for pool in &pool_data.raydium_pools {
            if let Ok(price) = self.calculate_raydium_price(pool).await {
                dex_prices.insert("raydium".to_string(), price);
            }
        }

        // Calculate Pump prices
        for pool in &pool_data.pump_pools {
            if let Ok(price) = self.calculate_pump_price(pool).await {
                dex_prices.insert("pump".to_string(), price);
            }
        }

        if dex_prices.len() >= 2 {
            // Find best buy and sell prices
            let (best_buy_dex, best_buy_price) = dex_prices
                .iter()
                .min_by(|(_, a), (_, b)| a.partial_cmp(b).unwrap())
                .unwrap();

            let (best_sell_dex, best_sell_price) = dex_prices
                .iter()
                .max_by(|(_, a), (_, b)| a.partial_cmp(b).unwrap())
                .unwrap();

            let price_spread = best_sell_price - best_buy_price;
            let potential_profit_percent = (price_spread / best_buy_price) * 100.0;

            // Only consider opportunities with significant spread
            if potential_profit_percent > 0.5 {
                opportunities.push(PriceComparison {
                    token_mint: token_mint.clone(),
                    dex_prices: dex_prices.clone(),
                    best_buy_price: *best_buy_price,
                    best_sell_price: *best_sell_price,
                    best_buy_dex: best_buy_dex.clone(),
                    best_sell_dex: best_sell_dex.clone(),
                    price_spread,
                    potential_profit_percent,
                    timestamp: Instant::now(),
                });
            }
        }

        Ok(opportunities)
    }

    /// Calculate price from Raydium pool
    async fn calculate_raydium_price(&self, pool: &RaydiumPool) -> Result<f64> {
        // This is a simplified calculation
        // In a real implementation, you would:
        // 1. Fetch the current reserves from the vaults
        // 2. Calculate the price based on the AMM formula
        // 3. Consider fees and slippage

        // For now, return a placeholder price
        Ok(1.0) // Placeholder
    }

    /// Calculate price from Pump pool
    async fn calculate_pump_price(&self, pool: &PumpPool) -> Result<f64> {
        // Similar to Raydium calculation
        Ok(1.0) // Placeholder
    }

    /// Get market statistics
    pub fn get_market_stats(&self) -> HashMap<String, usize> {
        let mut stats = HashMap::new();
        stats.insert("cached_prices".to_string(), self.price_cache.len());
        stats
    }

    /// Clear expired cache entries
    pub fn clear_expired_cache(&mut self) {
        let current_time = std::time::SystemTime::now()
            .duration_since(std::time::UNIX_EPOCH)
            .unwrap()
            .as_secs();

        self.price_cache.retain(|_, price| {
            current_time - price.timestamp < self.cache_ttl_seconds
        });
    }
}

/// Real-time price monitor
pub struct PriceMonitor {
    market_fetcher: MarketDataFetcher,
    monitoring_interval_ms: u64,
    price_threshold: f64,
}

impl PriceMonitor {
    pub fn new(
        rpc_client: Arc<RpcClient>,
        monitoring_interval_ms: u64,
        price_threshold: f64,
    ) -> Self {
        Self {
            market_fetcher: MarketDataFetcher::new(rpc_client),
            monitoring_interval_ms,
            price_threshold,
        }
    }

    /// Start monitoring prices for arbitrage opportunities
    pub async fn start_monitoring(&mut self, mints: Vec<String>) {
        info!("Starting price monitoring for {} tokens", mints.len());

        loop {
            for mint in &mints {
                match self.market_fetcher.fetch_token_price(mint).await {
                    Ok(price) => {
                        info!(
                            "Token {}: ${:.6} USD, {:.6} SOL (source: {})",
                            mint, price.price_usd, price.price_sol, price.source
                        );
                    }
                    Err(e) => {
                        warn!("Failed to fetch price for {}: {}", mint, e);
                    }
                }
            }

            // Clear expired cache
            self.market_fetcher.clear_expired_cache();

            // Wait before next monitoring cycle
            tokio::time::sleep(tokio::time::Duration::from_millis(
                self.monitoring_interval_ms,
            ))
            .await;
        }
    }
}

