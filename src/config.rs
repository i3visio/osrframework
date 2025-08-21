use std::env;
use dotenv::dotenv;

#[derive(Debug, Clone)]
pub struct Config {
    pub bot: BotConfig,
    pub routing: RoutingConfig,
    pub rpc: RpcConfig,
    pub spam: Option<SpamConfig>,
    pub wallet: WalletConfig,
    pub flashloan: Option<FlashloanConfig>,
}

#[derive(Debug, Clone)]
pub struct BotConfig {
    pub compute_unit_limit: u32,
}

#[derive(Debug, Clone)]
pub struct RoutingConfig {
    pub mint_config_list: Vec<MintConfig>,
}

#[derive(Debug, Clone)]
pub struct MintConfig {
    pub mint: String,

    pub raydium_pool_list: Option<Vec<String>>,
    pub raydium_cp_pool_list: Option<Vec<String>>,
    pub raydium_clmm_pool_list: Option<Vec<String>>,

    pub meteora_dlmm_pool_list: Option<Vec<String>>,
    pub meteora_damm_pool_list: Option<Vec<String>>,
    pub meteora_damm_v2_pool_list: Option<Vec<String>>,

    pub pump_pool_list: Option<Vec<String>>,

    pub whirlpool_pool_list: Option<Vec<String>>,

    pub solfi_pool_list: Option<Vec<String>>,

    pub vertigo_pool_list: Option<Vec<String>>,

    pub lookup_table_accounts: Option<Vec<String>>,
    pub process_delay: u64,
}

#[derive(Debug, Clone)]
pub struct RpcConfig {
    pub url: String,
}

#[derive(Debug, Clone)]
pub struct SpamConfig {
    pub enabled: bool,
    pub sending_rpc_urls: Vec<String>,
    pub compute_unit_price: u64,
    pub max_retries: Option<u64>,
}

#[derive(Debug, Clone)]
pub struct WalletConfig {
    pub private_key: String,
}

#[derive(Debug, Clone)]
pub struct FlashloanConfig {
    pub enabled: bool,
}

impl Config {
    pub fn load() -> anyhow::Result<Self> {
        // Load environment variables from .env file
        dotenv().ok();

        // Helper function to get environment variable with default
        fn get_env_or_default(key: &str, default: &str) -> String {
            env::var(key).unwrap_or_else(|_| default.to_string())
        }

        // Helper function to get boolean environment variable
        fn get_bool_env(key: &str, default: bool) -> bool {
            env::var(key)
                .map(|v| v.to_lowercase() == "true")
                .unwrap_or(default)
        }

        // Helper function to get u32 environment variable
        fn get_u32_env(key: &str, default: u32) -> u32 {
            env::var(key)
                .and_then(|v| v.parse().ok())
                .unwrap_or(default)
        }

        // Helper function to get u64 environment variable
        fn get_u64_env(key: &str, default: u64) -> u64 {
            env::var(key)
                .and_then(|v| v.parse().ok())
                .unwrap_or(default)
        }

        // Helper function to get optional u64 environment variable
        fn get_optional_u64_env(key: &str) -> Option<u64> {
            env::var(key).and_then(|v| v.parse().ok()).ok()
        }

        // Helper function to parse comma-separated string into Vec<String>
        fn parse_string_list(key: &str) -> Vec<String> {
            env::var(key)
                .map(|v| {
                    if v.is_empty() {
                        vec![]
                    } else {
                        v.split(',').map(|s| s.trim().to_string()).collect()
                    }
                })
                .unwrap_or_default()
        }

        // Build bot config
        let bot = BotConfig {
            compute_unit_limit: get_u32_env("BOT_COMPUTE_UNIT_LIMIT", 600000),
        };

        // Build RPC config
        let rpc = RpcConfig {
            url: get_env_or_default("RPC_URL", "https://api.mainnet-beta.solana.com"),
        };

        // Build wallet config
        let wallet = WalletConfig {
            private_key: get_env_or_default("WALLET_PRIVATE_KEY", ""),
        };

        // Build spam config (optional)
        let spam = if get_bool_env("SPAM_ENABLED", false) {
            Some(SpamConfig {
                enabled: true,
                sending_rpc_urls: parse_string_list("SPAM_SENDING_RPC_URLS"),
                compute_unit_price: get_u64_env("SPAM_COMPUTE_UNIT_PRICE", 1000),
                max_retries: get_optional_u64_env("SPAM_MAX_RETRIES"),
            })
        } else {
            None
        };

        // Build flashloan config (optional)
        let flashloan = if get_bool_env("FLASHLOAN_ENABLED", false) {
            Some(FlashloanConfig {
                enabled: true,
            })
        } else {
            None
        };

        // Build routing config with mint configurations
        let mut mint_config_list = Vec::new();
        
        // Try to load mint configurations from environment variables
        // This is a simplified approach - you might want to implement a more sophisticated
        // system for handling multiple mints
        let mint_1 = get_env_or_default("MINT_1", "");
        if !mint_1.is_empty() {
            let mint_config = MintConfig {
                mint: mint_1,
                raydium_pool_list: Some(parse_string_list("MINT_1_RAYDIUM_POOL_LIST")),
                raydium_cp_pool_list: None,
                raydium_clmm_pool_list: None,
                meteora_dlmm_pool_list: None,
                meteora_damm_pool_list: None,
                meteora_damm_v2_pool_list: None,
                pump_pool_list: Some(parse_string_list("MINT_1_PUMP_POOL_LIST")),
                whirlpool_pool_list: None,
                solfi_pool_list: None,
                vertigo_pool_list: None,
                lookup_table_accounts: None,
                process_delay: get_u64_env("MINT_1_PROCESS_DELAY", 1000),
            };
            mint_config_list.push(mint_config);
        }

        let routing = RoutingConfig {
            mint_config_list,
        };

        Ok(Config {
            bot,
            routing,
            rpc,
            spam,
            wallet,
            flashloan,
        })
    }
}
