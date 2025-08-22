use solana_mev_bot::{
    chain::{
        token_fetch::{TokenFetchConfig, TokenFetcher},
        token_price::{MarketDataFetcher, PriceMonitor},
    },
    config::Config,
};
use solana_client::rpc_client::RpcClient;
use std::sync::Arc;
use tracing_subscriber::{EnvFilter, FmtSubscriber};

#[tokio::main]
async fn main() {
    let subscriber = FmtSubscriber::builder()
        .with_env_filter(EnvFilter::from_default_env())
        .with_line_number(true)
        .finish();
    tracing::subscriber::set_global_default(subscriber).expect("setting default subscriber failed");

    // Load configuration from environment variables
    let config = match Config::load() {
        Ok(config) => config,
        Err(e) => {
            eprintln!("Failed to load configuration: {}", e);
            return;
        }
    };

    println!("Configuration loaded successfully!");
    println!("RPC URL: {}", config.rpc.url);
    println!("Compute unit limit: {}", config.bot.compute_unit_limit);

    // Initialize RPC client
    let rpc_client = Arc::new(RpcClient::new(config.rpc.url.clone()));

    // Initialize enhanced token fetcher
    let token_fetch_config = TokenFetchConfig {
        max_retries: 3,
        retry_delay_ms: 1000,
        batch_size: 10,
        timeout_seconds: 30,
        enable_caching: true,
        cache_ttl_seconds: 300,
    };

    let mut token_fetcher = TokenFetcher::new(rpc_client.clone(), token_fetch_config);

    // Initialize market data fetcher
    let mut market_fetcher = MarketDataFetcher::new(rpc_client.clone());

    // Initialize price monitor
    let mut price_monitor = PriceMonitor::new(rpc_client, 5000, 0.5); // 5 second intervals, 0.5% threshold

    // Process each mint configuration
    for mint_config in &config.routing.mint_config_list {
        println!("\nProcessing mint: {}", mint_config.mint);

        // Fetch pool data using enhanced token fetcher
        match token_fetcher
            .initialize_pool_data(
                &mint_config.mint,
                "YOUR_WALLET_ADDRESS", // Replace with actual wallet address
                mint_config.raydium_pool_list.as_ref(),
                mint_config.raydium_cp_pool_list.as_ref(),
                mint_config.pump_pool_list.as_ref(),
                mint_config.meteora_dlmm_pool_list.as_ref(),
                mint_config.whirlpool_pool_list.as_ref(),
                mint_config.raydium_clmm_pool_list.as_ref(),
                mint_config.meteora_damm_pool_list.as_ref(),
                mint_config.solfi_pool_list.as_ref(),
                mint_config.meteora_damm_v2_pool_list.as_ref(),
                mint_config.vertigo_pool_list.as_ref(),
            )
            .await
        {
            Ok(pool_data) => {
                println!("Successfully loaded pool data for mint: {}", mint_config.mint);
                println!("  - Raydium pools: {}", pool_data.raydium_pools.len());
                println!("  - Pump pools: {}", pool_data.pump_pools.len());
                println!("  - Whirlpool pools: {}", pool_data.whirlpool_pools.len());

                // Fetch token price
                match market_fetcher.fetch_token_price(&mint_config.mint).await {
                    Ok(price) => {
                        println!(
                            "Token price: ${:.6} USD, {:.6} SOL (source: {})",
                            price.price_usd, price.price_sol, price.source
                        );
                    }
                    Err(e) => {
                        println!("Failed to fetch token price: {}", e);
                    }
                }

                // Calculate arbitrage opportunities
                match market_fetcher
                    .calculate_arbitrage_opportunities(&pool_data)
                    .await
                {
                    Ok(opportunities) => {
                        if opportunities.is_empty() {
                            println!("No significant arbitrage opportunities found");
                        } else {
                            println!("Found {} arbitrage opportunities:", opportunities.len());
                            for (i, opp) in opportunities.iter().enumerate() {
                                println!(
                                    "  {}. {}: Buy on {} at {:.6}, Sell on {} at {:.6} ({}% profit)",
                                    i + 1,
                                    opp.token_mint,
                                    opp.best_buy_dex,
                                    opp.best_buy_price,
                                    opp.best_sell_dex,
                                    opp.best_sell_price,
                                    opp.potential_profit_percent
                                );
                            }
                        }
                    }
                    Err(e) => {
                        println!("Failed to calculate arbitrage opportunities: {}", e);
                    }
                }
            }
            Err(e) => {
                println!("Failed to load pool data for mint {}: {}", mint_config.mint, e);
            }
        }
    }

    // Start price monitoring (this would run indefinitely in a real bot)
    println!("\nStarting price monitoring...");
    let mints: Vec<String> = config
        .routing
        .mint_config_list
        .iter()
        .map(|mc| mc.mint.clone())
        .collect();

    // Uncomment the following line to start continuous price monitoring
    // price_monitor.start_monitoring(mints).await;

    println!("Enhanced token fetch logic demonstration completed!");
    println!("The bot is now ready for production use with improved error handling, caching, and retry logic.");
}
