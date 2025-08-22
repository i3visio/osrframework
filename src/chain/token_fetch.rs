use crate::{
    chain::{
        pools::{
            DlmmPool, MeteoraDAmmPool, MeteoraDAmmV2Pool, MintPoolData, PumpPool, RaydiumClmmPool,
            RaydiumCpPool, RaydiumPool, SolfiPool, VertigoPool, WhirlpoolPool,
        },
        SOL_MINT,
    },
    dex::{
        meteora::{
            constants::{
                damm_program_id, damm_v2_event_authority, damm_v2_pool_authority,
                damm_v2_program_id, dlmm_event_authority, dlmm_program_id,
            },
            dammv2_info::get_dammv2_info,
            dlmm_info::DlmmInfo,
        },
        pump::{
            amm_info::PumpAmmInfo,
            constants::{pump_fee_wallet, pump_program_id},
        },
        raydium::{
            amm_info::RaydiumAmmInfo,
            clmm_info::{
                get_tick_array_pubkeys, PoolState, POOL_TICK_ARRAY_BITMAP_SEED,
            },
            constants::*,
            cp_amm_info::RaydiumCpAmmInfo,
        },
        solfi::{constants::solfi_program_id, info::SolfiInfo},
        vertigo::{constants::vertigo_program_id, info::VertigoInfo, utils::derive_vault_address},
        whirlpool::{
            constants::whirlpool_program_id, state::Whirlpool as WhirlpoolState,
            utils::update_tick_array_accounts_for_onchain,
        },
    },
};
use anyhow::{anyhow, Result};
use solana_client::rpc_client::RpcClient;
use solana_sdk::{account::Account, pubkey::Pubkey};
use spl_associated_token_account;
use std::{
    collections::HashMap,
    str::FromStr,
    sync::Arc,
    time::{Duration, Instant},
};
use tokio::time::sleep;
use tracing::{debug, error, info, warn};

const TOKEN_2022_PROGRAM_ID: Pubkey = Pubkey::new_from_array([
    6, 221, 246, 225, 215, 101, 161, 147, 217, 203, 225, 70, 206, 235, 121, 172, 28, 180, 134, 244,
    64, 118, 252, 1, 16, 241, 37, 236, 114, 157, 18, 16,
]);

/// Configuration for token fetching
#[derive(Debug, Clone)]
pub struct TokenFetchConfig {
    pub max_retries: u32,
    pub retry_delay_ms: u64,
    pub batch_size: usize,
    pub timeout_seconds: u64,
    pub enable_caching: bool,
    pub cache_ttl_seconds: u64,
}

impl Default for TokenFetchConfig {
    fn default() -> Self {
        Self {
            max_retries: 3,
            retry_delay_ms: 1000,
            batch_size: 10,
            timeout_seconds: 30,
            enable_caching: true,
            cache_ttl_seconds: 300, // 5 minutes
        }
    }
}

/// Cache entry for token data
#[derive(Debug, Clone)]
struct CacheEntry {
    data: MintPoolData,
    timestamp: Instant,
}

/// Enhanced token fetcher with caching and retry logic
pub struct TokenFetcher {
    rpc_client: Arc<RpcClient>,
    config: TokenFetchConfig,
    cache: HashMap<String, CacheEntry>,
}

impl TokenFetcher {
    pub fn new(rpc_client: Arc<RpcClient>, config: TokenFetchConfig) -> Self {
        Self {
            rpc_client,
            config,
            cache: HashMap::new(),
        }
    }

    /// Initialize pool data with enhanced error handling and caching
    pub async fn initialize_pool_data(
        &mut self,
        mint: &str,
        wallet_account: &str,
        raydium_pools: Option<&Vec<String>>,
        raydium_cp_pools: Option<&Vec<String>>,
        pump_pools: Option<&Vec<String>>,
        dlmm_pools: Option<&Vec<String>>,
        whirlpool_pools: Option<&Vec<String>>,
        raydium_clmm_pools: Option<&Vec<String>>,
        meteora_damm_pools: Option<&Vec<String>>,
        solfi_pools: Option<&Vec<String>>,
        meteora_damm_v2_pools: Option<&Vec<String>>,
        vertigo_pools: Option<&Vec<String>>,
    ) -> Result<MintPoolData> {
        let cache_key = format!("{}_{}", mint, wallet_account);
        
        // Check cache first
        if self.config.enable_caching {
            if let Some(entry) = self.cache.get(&cache_key) {
                if entry.timestamp.elapsed().as_secs() < self.config.cache_ttl_seconds {
                    info!("Using cached pool data for mint: {}", mint);
                    return Ok(entry.data.clone());
                }
            }
        }

        info!("Initializing pool data for mint: {}", mint);
        let start_time = Instant::now();

        // Fetch mint account with retry logic
        let mint_pubkey = Pubkey::from_str(mint)?;
        let mint_account = self.fetch_account_with_retry(&mint_pubkey).await?;

        // Determine token program based on mint account owner
        let token_program = self.determine_token_program(&mint_account, mint)?;
        info!("Detected token program: {}", token_program);

        let mut pool_data = MintPoolData::new(mint, wallet_account, token_program)?;
        info!("Pool data initialized for mint: {}", mint);

        // Fetch pools in parallel batches for better performance
        let mut tasks = Vec::new();

        // Add pool fetching tasks
        if let Some(pools) = pump_pools {
            tasks.push(self.fetch_pump_pools(pools, &mint_pubkey));
        }
        if let Some(pools) = raydium_pools {
            tasks.push(self.fetch_raydium_pools(pools, &mint_pubkey));
        }
        if let Some(pools) = raydium_cp_pools {
            tasks.push(self.fetch_raydium_cp_pools(pools, &mint_pubkey));
        }
        if let Some(pools) = dlmm_pools {
            tasks.push(self.fetch_dlmm_pools(pools, &mint_pubkey));
        }
        if let Some(pools) = whirlpool_pools {
            tasks.push(self.fetch_whirlpool_pools(pools, &mint_pubkey));
        }
        if let Some(pools) = raydium_clmm_pools {
            tasks.push(self.fetch_raydium_clmm_pools(pools, &mint_pubkey));
        }
        if let Some(pools) = meteora_damm_pools {
            tasks.push(self.fetch_meteora_damm_pools(pools, &mint_pubkey));
        }
        if let Some(pools) = solfi_pools {
            tasks.push(self.fetch_solfi_pools(pools, &mint_pubkey));
        }
        if let Some(pools) = meteora_damm_v2_pools {
            tasks.push(self.fetch_meteora_damm_v2_pools(pools, &mint_pubkey));
        }
        if let Some(pools) = vertigo_pools {
            tasks.push(self.fetch_vertigo_pools(pools, &mint_pubkey));
        }

        // Execute all tasks concurrently
        let results = futures::future::join_all(tasks).await;

        // Merge results into pool_data
        for result in results {
            match result {
                Ok(pool_batch) => {
                    self.merge_pool_batch(&mut pool_data, pool_batch)?;
                }
                Err(e) => {
                    warn!("Failed to fetch some pools: {}", e);
                    // Continue with other pools instead of failing completely
                }
            }
        }

        // Cache the result
        if self.config.enable_caching {
            self.cache.insert(
                cache_key,
                CacheEntry {
                    data: pool_data.clone(),
                    timestamp: Instant::now(),
                },
            );
        }

        let elapsed = start_time.elapsed();
        info!(
            "Pool data initialization completed for mint: {} in {:?}",
            mint, elapsed
        );

        Ok(pool_data)
    }

    /// Fetch account with retry logic
    async fn fetch_account_with_retry(&self, pubkey: &Pubkey) -> Result<Account> {
        let mut last_error = None;
        
        for attempt in 0..self.config.max_retries {
            match self.rpc_client.get_account(pubkey) {
                Ok(account) => return Ok(account),
                Err(e) => {
                    last_error = Some(e);
                    if attempt < self.config.max_retries - 1 {
                        warn!(
                            "Failed to fetch account {} (attempt {}/{}), retrying in {}ms",
                            pubkey, attempt + 1, self.config.max_retries, self.config.retry_delay_ms
                        );
                        sleep(Duration::from_millis(self.config.retry_delay_ms)).await;
                    }
                }
            }
        }

        Err(anyhow!(
            "Failed to fetch account {} after {} attempts: {:?}",
            pubkey,
            self.config.max_retries,
            last_error
        ))
    }

    /// Determine token program from mint account
    fn determine_token_program(&self, mint_account: &Account, mint: &str) -> Result<Pubkey> {
        if mint_account.owner == spl_token::ID {
            Ok(spl_token::ID)
        } else if mint_account.owner == TOKEN_2022_PROGRAM_ID {
            Ok(TOKEN_2022_PROGRAM_ID)
        } else {
            Err(anyhow!("Unknown token program for mint: {}", mint))
        }
    }

    /// Fetch pump pools with enhanced error handling
    async fn fetch_pump_pools(
        &self,
        pools: &[String],
        mint_pubkey: &Pubkey,
    ) -> Result<Vec<PumpPool>> {
        let mut pump_pools = Vec::new();
        
        for pool_address in pools {
            match self.fetch_single_pump_pool(pool_address, mint_pubkey).await {
                Ok(pool) => {
                    pump_pools.push(pool);
                    info!("Pump pool added: {}", pool_address);
                }
                Err(e) => {
                    error!("Failed to fetch pump pool {}: {}", pool_address, e);
                    // Continue with other pools
                }
            }
        }
        
        Ok(pump_pools)
    }

    /// Fetch a single pump pool
    async fn fetch_single_pump_pool(
        &self,
        pool_address: &str,
        mint_pubkey: &Pubkey,
    ) -> Result<PumpPool> {
        let pump_pool_pubkey = Pubkey::from_str(pool_address)?;
        let account = self.fetch_account_with_retry(&pump_pool_pubkey).await?;

        if account.owner != pump_program_id() {
            return Err(anyhow!(
                "Pump pool account is not owned by the Pump program: {}",
                pool_address
            ));
        }

        let amm_info = PumpAmmInfo::load_checked(&account.data)?;
        
        let (sol_vault, token_vault) = if sol_mint() == amm_info.base_mint {
            (
                amm_info.pool_base_token_account,
                amm_info.pool_quote_token_account,
            )
        } else if sol_mint() == amm_info.quote_mint {
            (
                amm_info.pool_quote_token_account,
                amm_info.pool_base_token_account,
            )
        } else {
            (
                amm_info.pool_quote_token_account,
                amm_info.pool_base_token_account,
            )
        };

        let fee_token_wallet = spl_associated_token_account::get_associated_token_address(
            &pump_fee_wallet(),
            &amm_info.quote_mint,
        );

        let coin_creator_vault_ata = spl_associated_token_account::get_associated_token_address(
            &amm_info.coin_creator_vault_authority,
            &amm_info.quote_mint,
        );

        let (token_mint, base_mint) = if *mint_pubkey == amm_info.base_mint {
            (amm_info.base_mint, amm_info.quote_mint)
        } else {
            (amm_info.quote_mint, amm_info.base_mint)
        };

        Ok(PumpPool {
            pool: pump_pool_pubkey,
            token_vault,
            sol_vault,
            fee_token_wallet,
            coin_creator_vault_ata,
            coin_creator_vault_authority: amm_info.coin_creator_vault_authority,
            token_mint,
            base_mint,
        })
    }

    /// Fetch Raydium pools
    async fn fetch_raydium_pools(
        &self,
        pools: &[String],
        mint_pubkey: &Pubkey,
    ) -> Result<Vec<RaydiumPool>> {
        let mut raydium_pools = Vec::new();
        
        for pool_address in pools {
            match self.fetch_single_raydium_pool(pool_address, mint_pubkey).await {
                Ok(pool) => {
                    raydium_pools.push(pool);
                    info!("Raydium pool added: {}", pool_address);
                }
                Err(e) => {
                    error!("Failed to fetch Raydium pool {}: {}", pool_address, e);
                }
            }
        }
        
        Ok(raydium_pools)
    }

    /// Fetch a single Raydium pool
    async fn fetch_single_raydium_pool(
        &self,
        pool_address: &str,
        mint_pubkey: &Pubkey,
    ) -> Result<RaydiumPool> {
        let raydium_pool_pubkey = Pubkey::from_str(pool_address)?;
        let account = self.fetch_account_with_retry(&raydium_pool_pubkey).await?;

        if account.owner != raydium_program_id() {
            return Err(anyhow!(
                "Raydium pool account is not owned by the Raydium program: {}",
                pool_address
            ));
        }

        let amm_info = RaydiumAmmInfo::load_checked(&account.data)?;
        
        let (sol_vault, token_vault) = if sol_mint() == amm_info.base_mint {
            (
                amm_info.pool_base_token_account,
                amm_info.pool_quote_token_account,
            )
        } else if sol_mint() == amm_info.quote_mint {
            (
                amm_info.pool_quote_token_account,
                amm_info.pool_base_token_account,
            )
        } else {
            (
                amm_info.pool_quote_token_account,
                amm_info.pool_base_token_account,
            )
        };

        let (token_mint, base_mint) = if *mint_pubkey == amm_info.base_mint {
            (amm_info.base_mint, amm_info.quote_mint)
        } else {
            (amm_info.quote_mint, amm_info.base_mint)
        };

        Ok(RaydiumPool {
            pool: raydium_pool_pubkey,
            token_vault,
            sol_vault,
            token_mint,
            base_mint,
        })
    }

    // Placeholder methods for other pool types - implement similar to above
    async fn fetch_raydium_cp_pools(
        &self,
        _pools: &[String],
        _mint_pubkey: &Pubkey,
    ) -> Result<Vec<RaydiumCpPool>> {
        // TODO: Implement Raydium CP pool fetching
        Ok(Vec::new())
    }

    async fn fetch_dlmm_pools(
        &self,
        _pools: &[String],
        _mint_pubkey: &Pubkey,
    ) -> Result<Vec<DlmmPool>> {
        // TODO: Implement DLMM pool fetching
        Ok(Vec::new())
    }

    async fn fetch_whirlpool_pools(
        &self,
        _pools: &[String],
        _mint_pubkey: &Pubkey,
    ) -> Result<Vec<WhirlpoolPool>> {
        // TODO: Implement Whirlpool fetching
        Ok(Vec::new())
    }

    async fn fetch_raydium_clmm_pools(
        &self,
        _pools: &[String],
        _mint_pubkey: &Pubkey,
    ) -> Result<Vec<RaydiumClmmPool>> {
        // TODO: Implement Raydium CLMM pool fetching
        Ok(Vec::new())
    }

    async fn fetch_meteora_damm_pools(
        &self,
        _pools: &[String],
        _mint_pubkey: &Pubkey,
    ) -> Result<Vec<MeteoraDAmmPool>> {
        // TODO: Implement Meteora DAmm pool fetching
        Ok(Vec::new())
    }

    async fn fetch_solfi_pools(
        &self,
        _pools: &[String],
        _mint_pubkey: &Pubkey,
    ) -> Result<Vec<SolfiPool>> {
        // TODO: Implement Solfi pool fetching
        Ok(Vec::new())
    }

    async fn fetch_meteora_damm_v2_pools(
        &self,
        _pools: &[String],
        _mint_pubkey: &Pubkey,
    ) -> Result<Vec<MeteoraDAmmV2Pool>> {
        // TODO: Implement Meteora DAmm V2 pool fetching
        Ok(Vec::new())
    }

    async fn fetch_vertigo_pools(
        &self,
        _pools: &[String],
        _mint_pubkey: &Pubkey,
    ) -> Result<Vec<VertigoPool>> {
        // TODO: Implement Vertigo pool fetching
        Ok(Vec::new())
    }

    /// Merge pool batch into main pool data
    fn merge_pool_batch(&self, pool_data: &mut MintPoolData, pool_batch: PoolBatch) -> Result<()> {
        // TODO: Implement merging logic for different pool types
        Ok(())
    }

    /// Clear expired cache entries
    pub fn clear_expired_cache(&mut self) {
        let now = Instant::now();
        self.cache.retain(|_, entry| {
            now.duration_since(entry.timestamp).as_secs() < self.config.cache_ttl_seconds
        });
    }

    /// Get cache statistics
    pub fn get_cache_stats(&self) -> (usize, usize) {
        let total_entries = self.cache.len();
        let expired_entries = self
            .cache
            .values()
            .filter(|entry| {
                entry.timestamp.elapsed().as_secs() >= self.config.cache_ttl_seconds
            })
            .count();
        (total_entries, expired_entries)
    }
}

/// Batch of pools for concurrent processing
#[derive(Debug)]
struct PoolBatch {
    pump_pools: Vec<PumpPool>,
    raydium_pools: Vec<RaydiumPool>,
    raydium_cp_pools: Vec<RaydiumCpPool>,
    dlmm_pools: Vec<DlmmPool>,
    whirlpool_pools: Vec<WhirlpoolPool>,
    raydium_clmm_pools: Vec<RaydiumClmmPool>,
    meteora_damm_pools: Vec<MeteoraDAmmPool>,
    solfi_pools: Vec<SolfiPool>,
    meteora_damm_v2_pools: Vec<MeteoraDAmmV2Pool>,
    vertigo_pools: Vec<VertigoPool>,
}

impl PoolBatch {
    fn new() -> Self {
        Self {
            pump_pools: Vec::new(),
            raydium_pools: Vec::new(),
            raydium_cp_pools: Vec::new(),
            dlmm_pools: Vec::new(),
            whirlpool_pools: Vec::new(),
            raydium_clmm_pools: Vec::new(),
            meteora_damm_pools: Vec::new(),
            solfi_pools: Vec::new(),
            meteora_damm_v2_pools: Vec::new(),
            vertigo_pools: Vec::new(),
        }
    }
}

