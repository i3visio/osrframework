use super::constants::sol_mint;
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
            constants::{
                pump_fee_wallet, pump_program_id,
            },
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
use solana_client::rpc_client::RpcClient;
use solana_sdk::{account::Account, pubkey::Pubkey};
use spl_associated_token_account;
use std::{collections::HashMap, str::FromStr, sync::Arc};
use tracing::{debug, error, info};

const TOKEN_2022_PROGRAM_ID: Pubkey = Pubkey::new_from_array([
    6, 221, 246, 225, 215, 101, 161, 147, 217, 203, 225, 70, 206, 235, 121, 172, 28, 180, 134, 244,
    64, 118, 252, 1, 16, 241, 37, 236, 114, 157, 18, 16,
]);

pub async fn initialize_pool_data(
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
    rpc_client: Arc<RpcClient>,
) -> anyhow::Result<MintPoolData> {
    info!("Initializing pool data for mint: {}", mint);

    // Fetch mint account to determine token program
    let mint_pubkey = Pubkey::from_str(mint)?;
    let mint_account = rpc_client.get_account(&mint_pubkey)?;

    // Determine token program based on mint account owner
    let token_program = if mint_account.owner == spl_token::ID {
        spl_token::ID
    } else if mint_account.owner == TOKEN_2022_PROGRAM_ID {
        TOKEN_2022_PROGRAM_ID
    } else {
        return Err(anyhow::anyhow!("Unknown token program for mint: {}", mint));
    };

    info!("Detected token program: {}", token_program);
    let mut pool_data = MintPoolData::new(mint, wallet_account, token_program)?;
    info!("Pool data initialized for mint: {}", mint);

    if let Some(pools) = pump_pools {
        for pool_address in pools {
            let pump_pool_pubkey = Pubkey::from_str(pool_address)?;

            match rpc_client.get_account(&pump_pool_pubkey) {
                Ok(account) => {
                    if account.owner != pump_program_id() {
                        error!(
                            "Error: Pump pool account is not owned by the Pump program. Expected: {}, Actual: {}",
                            pump_program_id(), account.owner
                        );
                        return Err(anyhow::anyhow!(
                            "Pump pool account is not owned by the Pump program"
                        ));
                    }

                    match PumpAmmInfo::load_checked(&account.data) {
                        Ok(amm_info) => {
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

                            let fee_token_wallet =
                                spl_associated_token_account::get_associated_token_address(
                                    &pump_fee_wallet(),
                                    &amm_info.quote_mint,
                                );

                            let coin_creator_vault_ata =
                                spl_associated_token_account::get_associated_token_address(
                                    &amm_info.coin_creator_vault_authority,
                                    &amm_info.quote_mint,
                                );

                            // Determine token_mint and base_mint
                            let (token_mint, base_mint) = if mint_pubkey == amm_info.base_mint {
                                (amm_info.base_mint, amm_info.quote_mint)
                            } else {
                                (amm_info.quote_mint, amm_info.base_mint)
                            };
                            
                            pool_data.add_pump_pool(
                                pool_address,
                                &token_vault.to_string(),
                                &sol_vault.to_string(),
                                &fee_token_wallet.to_string(),
                                &coin_creator_vault_ata.to_string(),
                                &amm_info.coin_creator_vault_authority.to_string(),
                                &token_mint.to_string(),
                                &base_mint.to_string(),
                            )?;
                            info!("Pump pool added: {}", pool_address);
                            info!("    Base mint: {}", amm_info.base_mint.to_string());
                            info!("    Quote mint: {}", amm_info.quote_mint.to_string());
                            info!("    Token vault: {}", token_vault.to_string());
                            info!("    Sol vault: {}", sol_vault.to_string());
                            info!("    Fee token wallet: {}", fee_token_wallet.to_string());
                            info!(
                                "    Coin creator vault ata: {}",
                                coin_creator_vault_ata.to_string()
                            );
                            info!(
                                "    Coin creator vault authority: {}",
                                amm_info.coin_creator_vault_authority.to_string()
                            );
                            info!("    Initialized Pump pool: {}\n", pump_pool_pubkey);
                        }
                        Err(e) => {
                            error!(
                                "Error parsing AmmInfo from Pump pool {}: {:?}",
                                pump_pool_pubkey, e
                            );
                            return Err(e);
                        }
                    }
                }
                Err(e) => {
                    error!(
                        "Error fetching Pump pool account {}: {:?}",
                        pump_pool_pubkey, e
                    );
                    return Err(anyhow::anyhow!("Error fetching Pump pool account"));
                }
            }
        }
    }

    if let Some(pools) = raydium_pools {
        for pool_address in pools {
            let raydium_pool_pubkey = Pubkey::from_str(pool_address)?;

            match rpc_client.get_account(&raydium_pool_pubkey) {
                Ok(account) => {
                    if account.owner != raydium_program_id() {
                        error!(
                            "Error: Raydium pool account is not owned by the Raydium program. Expected: {}, Actual: {}",
                            raydium_program_id(), account.owner
                        );
                        return Err(anyhow::anyhow!(
                            "Raydium pool account is not owned by the Raydium program"
                        ));
                    }

                    match RaydiumAmmInfo::load_checked(&account.data) {
                        Ok(amm_info) => {
                            if amm_info.coin_mint != pool_data.mint
                                && amm_info.pc_mint != pool_data.mint
                            {
                                error!(
                                    "Mint {} is not present in Raydium pool {}, skipping",
                                    pool_data.mint, raydium_pool_pubkey
                                );
                                return Err(anyhow::anyhow!(
                                    "Invalid Raydium pool: {}",
                                    raydium_pool_pubkey
                                ));
                            }

                            if amm_info.coin_mint != sol_mint() && amm_info.pc_mint != sol_mint() {
                                error!(
                                    "SOL is not present in Raydium pool {}",
                                    raydium_pool_pubkey
                                );
                                return Err(anyhow::anyhow!(
                                    "SOL is not present in Raydium pool: {}",
                                    raydium_pool_pubkey
                                ));
                            }

                            let (sol_vault, token_vault) = if sol_mint() == amm_info.coin_mint {
                                (amm_info.coin_vault, amm_info.pc_vault)
                            } else {
                                (amm_info.pc_vault, amm_info.coin_vault)
                            };

                            // Determine token_mint and base_mint
                            let (token_mint, base_mint) = if mint_pubkey == amm_info.coin_mint {
                                (amm_info.coin_mint, amm_info.pc_mint)
                            } else {
                                (amm_info.pc_mint, amm_info.coin_mint)
                            };
                            
                            pool_data.add_raydium_pool(
                                pool_address,
                                &token_vault.to_string(),
                                &sol_vault.to_string(),
                                &token_mint.to_string(),
                                &base_mint.to_string(),
                            )?;
                            info!("Raydium pool added: {}", pool_address);
                            info!("    Coin mint: {}", amm_info.coin_mint.to_string());
                            info!("    PC mint: {}", amm_info.pc_mint.to_string());
                            info!("    Token vault: {}", token_vault.to_string());
                            info!("    Sol vault: {}", sol_vault.to_string());
                            info!("    Initialized Raydium pool: {}\n", raydium_pool_pubkey);
                        }
                        Err(e) => {
                            error!(
                                "Error parsing AmmInfo from Raydium pool {}: {:?}",
                                raydium_pool_pubkey, e
                            );
                            return Err(e);
                        }
                    }
                }
                Err(e) => {
                    error!(
                        "Error fetching Raydium pool account {}: {:?}",
                        raydium_pool_pubkey, e
                    );
                    return Err(anyhow::anyhow!("Error fetching Raydium pool account"));
                }
            }
        }
    }

    if let Some(pools) = raydium_cp_pools {
        for pool_address in pools {
            let raydium_cp_pool_pubkey = Pubkey::from_str(pool_address)?;

            match rpc_client.get_account(&raydium_cp_pool_pubkey) {
                Ok(account) => {
                    if account.owner != raydium_cp_program_id() {
                        error!(
                            "Error: Raydium CP pool account is not owned by the Raydium CP program. Expected: {}, Actual: {}",
                            raydium_cp_program_id(), account.owner
                        );
                        return Err(anyhow::anyhow!(
                            "Raydium CP pool account is not owned by the Raydium CP program"
                        ));
                    }

                    match RaydiumCpAmmInfo::load_checked(&account.data) {
                        Ok(amm_info) => {
                            if amm_info.token_0_mint != pool_data.mint
                                && amm_info.token_1_mint != pool_data.mint
                            {
                                error!(
                                    "Mint {} is not present in Raydium CP pool {}, skipping",
                                    pool_data.mint, raydium_cp_pool_pubkey
                                );
                                return Err(anyhow::anyhow!(
                                    "Invalid Raydium CP pool: {}",
                                    raydium_cp_pool_pubkey
                                ));
                            }

                            let (sol_vault, token_vault) = if sol_mint() == amm_info.token_0_mint {
                                (amm_info.token_0_vault, amm_info.token_1_vault)
                            } else if sol_mint() == amm_info.token_1_mint {
                                (amm_info.token_1_vault, amm_info.token_0_vault)
                            } else {
                                error!(
                                    "SOL is not present in Raydium CP pool {}",
                                    raydium_cp_pool_pubkey
                                );
                                return Err(anyhow::anyhow!(
                                    "SOL is not present in Raydium CP pool: {}",
                                    raydium_cp_pool_pubkey
                                ));
                            };

                            // Determine token_mint and base_mint
                            let (token_mint, base_mint) = if mint_pubkey == amm_info.token_0_mint {
                                (amm_info.token_0_mint, amm_info.token_1_mint)
                            } else {
                                (amm_info.token_1_mint, amm_info.token_0_mint)
                            };
                            
                            pool_data.add_raydium_cp_pool(
                                pool_address,
                                &token_vault.to_string(),
                                &sol_vault.to_string(),
                                &amm_info.amm_config.to_string(),
                                &amm_info.observation_key.to_string(),
                                &token_mint.to_string(),
                                &base_mint.to_string(),
                            )?;
                            info!("Raydium CP pool added: {}", pool_address);
                            info!("    Token vault: {}", token_vault.to_string());
                            info!("    Sol vault: {}", sol_vault.to_string());
                            info!("    AMM Config: {}", amm_info.amm_config.to_string());
                            info!(
                                "    Observation Key: {}\n",
                                amm_info.observation_key.to_string()
                            );
                        }
                        Err(e) => {
                            error!(
                                "Error parsing AmmInfo from Raydium CP pool {}: {:?}",
                                raydium_cp_pool_pubkey, e
                            );
                            return Err(e);
                        }
                    }
                }
                Err(e) => {
                    error!(
                        "Error fetching Raydium CP pool account {}: {:?}",
                        raydium_cp_pool_pubkey, e
                    );
                    return Err(anyhow::anyhow!("Error fetching Raydium CP pool account"));
                }
            }
        }
    }
    if let Some(pools) = dlmm_pools {
        for pool_address in pools {
            let dlmm_pool_pubkey = Pubkey::from_str(pool_address)?;

            match rpc_client.get_account(&dlmm_pool_pubkey) {
                Ok(account) => {
                    if account.owner != dlmm_program_id() {
                        error!(
                            "Error: DLMM pool account is not owned by the DLMM program. Expected: {}, Actual: {}",
                            dlmm_program_id(), account.owner
                        );
                        return Err(anyhow::anyhow!(
                            "DLMM pool account is not owned by the DLMM program"
                        ));
                    }

                    match DlmmInfo::load_checked(&account.data) {
                        Ok(amm_info) => {
                            let sol_mint = sol_mint();
                            let (token_vault, sol_vault) =
                                amm_info.get_token_and_sol_vaults(&pool_data.mint, &sol_mint);

                            let bin_arrays = match amm_info.calculate_bin_arrays(&dlmm_pool_pubkey)
                            {
                                Ok(arrays) => arrays,
                                Err(e) => {
                                    error!(
                                        "Error calculating bin arrays for DLMM pool {}: {:?}",
                                        dlmm_pool_pubkey, e
                                    );
                                    return Err(e);
                                }
                            };

                            let bin_array_strings: Vec<String> =
                                bin_arrays.iter().map(|pubkey| pubkey.to_string()).collect();
                            let bin_array_str_refs: Vec<&str> =
                                bin_array_strings.iter().map(|s| s.as_str()).collect();

                            // Determine token_mint and base_mint
                            let (token_mint, base_mint) = if mint_pubkey == amm_info.token_x_mint {
                                (amm_info.token_x_mint, amm_info.token_y_mint)
                            } else {
                                (amm_info.token_y_mint, amm_info.token_x_mint)
                            };
                            
                            pool_data.add_dlmm_pool(
                                pool_address,
                                &token_vault.to_string(),
                                &sol_vault.to_string(),
                                &amm_info.oracle.to_string(),
                                bin_array_str_refs,
                                None, // memo_program
                                &token_mint.to_string(),
                                &base_mint.to_string(),
                            )?;

                            info!("DLMM pool added: {}", pool_address);
                            info!("    Token X Mint: {}", amm_info.token_x_mint.to_string());
                            info!("    Token Y Mint: {}", amm_info.token_y_mint.to_string());
                            info!("    Token vault: {}", token_vault.to_string());
                            info!("    Sol vault: {}", sol_vault.to_string());
                            info!("    Oracle: {}", amm_info.oracle.to_string());
                            info!("    Active ID: {}", amm_info.active_id);

                            for (i, array) in bin_array_strings.iter().enumerate() {
                                info!("    Bin Array {}: {}", i, array);
                            }
                            info!("");
                        }
                        Err(e) => {
                            error!(
                                "Error parsing AmmInfo from DLMM pool {}: {:?}",
                                dlmm_pool_pubkey, e
                            );
                            return Err(e);
                        }
                    }
                }
                Err(e) => {
                    error!(
                        "Error fetching DLMM pool account {}: {:?}",
                        dlmm_pool_pubkey, e
                    );
                    return Err(anyhow::anyhow!("Error fetching DLMM pool account"));
                }
            }
        }
    }

    if let Some(pools) = whirlpool_pools {
        for pool_address in pools {
            let whirlpool_pool_pubkey = Pubkey::from_str(pool_address)?;

            match rpc_client.get_account(&whirlpool_pool_pubkey) {
                Ok(account) => {
                    if account.owner != whirlpool_program_id() {
                        error!(
                            "Error: Whirlpool pool account is not owned by the Whirlpool program. Expected: {}, Actual: {}",
                            whirlpool_program_id(), account.owner
                        );
                        return Err(anyhow::anyhow!(
                            "Whirlpool pool account is not owned by the Whirlpool program"
                        ));
                    }

                    match WhirlpoolState::try_deserialize(&account.data) {
                        Ok(whirlpool) => {
                            if whirlpool.token_mint_a != pool_data.mint
                                && whirlpool.token_mint_b != pool_data.mint
                            {
                                error!(
                                    "Mint {} is not present in Whirlpool pool {}, skipping",
                                    pool_data.mint, whirlpool_pool_pubkey
                                );
                                return Err(anyhow::anyhow!(
                                    "Invalid Whirlpool pool: {}",
                                    whirlpool_pool_pubkey
                                ));
                            }

                            let sol_mint = sol_mint();
                            let (sol_vault, token_vault) = if sol_mint == whirlpool.token_mint_a {
                                (whirlpool.token_vault_a, whirlpool.token_vault_b)
                            } else if sol_mint == whirlpool.token_mint_b {
                                (whirlpool.token_vault_b, whirlpool.token_vault_a)
                            } else {
                                error!(
                                    "SOL is not present in Whirlpool pool {}",
                                    whirlpool_pool_pubkey
                                );
                                return Err(anyhow::anyhow!(
                                    "SOL is not present in Whirlpool pool: {}",
                                    whirlpool_pool_pubkey
                                ));
                            };

                            let whirlpool_oracle = Pubkey::find_program_address(
                                &[b"oracle", whirlpool_pool_pubkey.as_ref()],
                                &whirlpool_program_id(),
                            )
                            .0;

                            let mut whirlpool_tick_arrays = Vec::new();
                            let a_to_b = whirlpool.token_mint_a == mint_pubkey;
                            update_tick_array_accounts_for_onchain(
                                &whirlpool_pool_pubkey,
                                &mut whirlpool_tick_arrays,
                                a_to_b,
                                whirlpool.tick_spacing,
                                whirlpool.tick_current_index,
                            );

                            let tick_array_strings: Vec<String> = whirlpool_tick_arrays
                                .iter()
                                .map(|pubkey| pubkey.to_string())
                                .collect();

                            let tick_array_str_refs: Vec<&str> =
                                tick_array_strings.iter().map(|s| s.as_str()).collect();

                            // Determine token_mint and base_mint
                            let (token_mint, base_mint) = if mint_pubkey == whirlpool.token_mint_a {
                                (whirlpool.token_mint_a, whirlpool.token_mint_b)
                            } else {
                                (whirlpool.token_mint_b, whirlpool.token_mint_a)
                            };
                            
                            pool_data.add_whirlpool_pool(
                                pool_address,
                                &whirlpool_oracle.to_string(),
                                &token_vault.to_string(),
                                &sol_vault.to_string(),
                                tick_array_str_refs,
                                None, // memo_program
                                &token_mint.to_string(),
                                &base_mint.to_string(),
                            )?;

                            info!("Whirlpool pool added: {}", pool_address);
                            info!("    Token mint A: {}", whirlpool.token_mint_a.to_string());
                            info!("    Token mint B: {}", whirlpool.token_mint_b.to_string());
                            info!("    Token vault: {}", token_vault.to_string());
                            info!("    Sol vault: {}", sol_vault.to_string());
                            info!("    Oracle: {}", whirlpool_oracle.to_string());

                            for (i, array) in tick_array_strings.iter().enumerate() {
                                info!("    Tick Array {}: {}", i, array);
                            }
                            info!("");
                        }
                        Err(e) => {
                            error!(
                                "Error parsing Whirlpool data from pool {}: {:?}",
                                whirlpool_pool_pubkey, e
                            );
                            return Err(anyhow::anyhow!("Error parsing Whirlpool data"));
                        }
                    }
                }
                Err(e) => {
                    error!(
                        "Error fetching Whirlpool pool account {}: {:?}",
                        whirlpool_pool_pubkey, e
                    );
                    return Err(anyhow::anyhow!("Error fetching Whirlpool pool account"));
                }
            }
        }
    }

    if let Some(pools) = raydium_clmm_pools {
        for pool_address in pools {
            let raydium_clmm_program_id = raydium_clmm_program_id();

            match rpc_client.get_account(&Pubkey::from_str(pool_address)?) {
                Ok(account) => {
                    if account.owner != raydium_clmm_program_id {
                        error!(
                            "Raydium CLMM pool {} is not owned by the Raydium CLMM program, skipping",
                            pool_address
                        );
                        continue;
                    }

                    match PoolState::load_checked(&account.data) {
                        Ok(raydium_clmm) => {
                            if raydium_clmm.token_mint_0 != pool_data.mint
                                && raydium_clmm.token_mint_1 != pool_data.mint
                            {
                                error!(
                                    "Mint {} is not present in Raydium CLMM pool {}, skipping",
                                    pool_data.mint, pool_address
                                );
                                continue;
                            }

                            let sol_mint = sol_mint();
                            let (token_vault, sol_vault) = if sol_mint == raydium_clmm.token_mint_0
                            {
                                (raydium_clmm.token_vault_1, raydium_clmm.token_vault_0)
                            } else if sol_mint == raydium_clmm.token_mint_1 {
                                (raydium_clmm.token_vault_0, raydium_clmm.token_vault_1)
                            } else {
                                error!("SOL is not present in Raydium CLMM pool {}", pool_address);
                                continue;
                            };

                            let tick_array_pubkeys = get_tick_array_pubkeys(
                                &Pubkey::from_str(pool_address)?,
                                raydium_clmm.tick_current,
                                raydium_clmm.tick_spacing,
                                &[-1, 0, 1],
                                &raydium_clmm_program_id,
                            )?;

                            let tick_array_strings: Vec<String> = tick_array_pubkeys
                                .iter()
                                .map(|pubkey| pubkey.to_string())
                                .collect();

                            let tick_array_str_refs: Vec<&str> =
                                tick_array_strings.iter().map(|s| s.as_str()).collect();

                            // Determine token_mint and base_mint
                            let (token_mint, base_mint) = if mint_pubkey == raydium_clmm.token_mint_0 {
                                (raydium_clmm.token_mint_0, raydium_clmm.token_mint_1)
                            } else {
                                (raydium_clmm.token_mint_1, raydium_clmm.token_mint_0)
                            };
                            
                            pool_data.add_raydium_clmm_pool(
                                pool_address,
                                &raydium_clmm.amm_config.to_string(),
                                &raydium_clmm.observation_key.to_string(),
                                &token_vault.to_string(),
                                &sol_vault.to_string(),
                                tick_array_str_refs,
                                None, // memo_program
                                &token_mint.to_string(),
                                &base_mint.to_string(),
                            )?;

                            info!("Raydium CLMM pool added: {}", pool_address);
                            info!(
                                "    Token mint 0: {}",
                                raydium_clmm.token_mint_0.to_string()
                            );
                            info!(
                                "    Token mint 1: {}",
                                raydium_clmm.token_mint_1.to_string()
                            );
                            info!("    Token vault: {}", token_vault.to_string());
                            info!("    Sol vault: {}", sol_vault.to_string());
                            info!("    AMM config: {}", raydium_clmm.amm_config.to_string());
                            info!(
                                "    Observation key: {}",
                                raydium_clmm.observation_key.to_string()
                            );

                            for (i, array) in tick_array_strings.iter().enumerate() {
                                info!("    Tick Array {}: {}", i, array);
                            }
                            info!("");
                        }
                        Err(e) => {
                            error!(
                                "Error parsing Raydium CLMM data from pool {}: {:?}",
                                pool_address, e
                            );
                            continue;
                        }
                    }
                }
                Err(e) => {
                    error!(
                        "Error fetching Raydium CLMM pool account {}: {:?}",
                        pool_address, e
                    );
                    continue;
                }
            }
        }
    }

    if let Some(pools) = meteora_damm_pools {
        for pool_address in pools {
            let meteora_damm_pool_pubkey = Pubkey::from_str(pool_address)?;

            match rpc_client.get_account(&meteora_damm_pool_pubkey) {
                Ok(account) => {
                    if account.owner != damm_program_id() {
                        error!(
                            "Error: Meteora DAMM pool account is not owned by the Meteora DAMM program. Expected: {}, Actual: {}",
                            damm_program_id(), account.owner
                        );
                        return Err(anyhow::anyhow!(
                            "Meteora DAMM pool account is not owned by the Meteora DAMM program"
                        ));
                    }

                    let damm_pool = MeteoraDAmmPool {
                        pool: meteora_damm_pool_pubkey,
                        token_x_vault: Pubkey::new_from_array(
                            account.data[168..200].try_into().unwrap(),
                        ),
                        token_sol_vault: Pubkey::new_from_array(
                            account.data[200..232].try_into().unwrap(),
                        ),
                        token_x_token_vault: Pubkey::new_from_array(
                            account.data[232..264].try_into().unwrap(),
                        ),
                        token_sol_token_vault: Pubkey::new_from_array(
                            account.data[264..296].try_into().unwrap(),
                        ),
                        token_x_lp_mint: Pubkey::new_from_array(
                            account.data[296..328].try_into().unwrap(),
                        ),
                        token_sol_lp_mint: Pubkey::new_from_array(
                            account.data[328..360].try_into().unwrap(),
                        ),
                        token_x_pool_lp: Pubkey::new_from_array(
                            account.data[360..392].try_into().unwrap(),
                        ),
                        token_sol_pool_lp: Pubkey::new_from_array(
                            account.data[392..424].try_into().unwrap(),
                        ),
                        admin_token_fee_x: Pubkey::new_from_array(
                            account.data[424..456].try_into().unwrap(),
                        ),
                        admin_token_fee_sol: Pubkey::new_from_array(
                            account.data[456..488].try_into().unwrap(),
                        ),
                        token_mint: if mint_pubkey
                            == Pubkey::new_from_array(account.data[104..136].try_into().unwrap())
                        {
                            Pubkey::new_from_array(account.data[104..136].try_into().unwrap())
                        } else {
                            Pubkey::new_from_array(account.data[136..168].try_into().unwrap())
                        },
                        base_mint: if mint_pubkey
                            == Pubkey::new_from_array(account.data[104..136].try_into().unwrap())
                        {
                            Pubkey::new_from_array(account.data[136..168].try_into().unwrap())
                        } else {
                            Pubkey::new_from_array(account.data[104..136].try_into().unwrap())
                        },
                    };

                    info!("Meteora DAMM pool added: {}", pool_address);
                    info!(
                        "    Token X vault: {}",
                        damm_pool.token_x_vault.to_string()
                    );
                    info!(
                        "    SOL vault: {}",
                        damm_pool.token_sol_vault.to_string()
                    );
                    info!(
                        "    Token X LP mint: {}",
                        damm_pool.token_x_lp_mint.to_string()
                    );
                    info!(
                        "    SOL LP mint: {}",
                        damm_pool.token_sol_lp_mint.to_string()
                    );
                    info!(
                        "    Token X pool LP: {}",
                        damm_pool.token_x_pool_lp.to_string()
                    );
                    info!(
                        "    SOL pool LP: {}",
                        damm_pool.token_sol_pool_lp.to_string()
                    );
                    info!(
                        "    Token X admin fee: {}",
                        damm_pool.admin_token_fee_x.to_string()
                    );
                    info!(
                        "    SOL admin fee: {}",
                        damm_pool.admin_token_fee_sol.to_string()
                    );
                    info!("");
                }
                Err(e) => {
                    error!(
                        "Error fetching Meteora DAMM pool account {}: {:?}",
                        meteora_damm_pool_pubkey, e
                    );
                    return Err(anyhow::anyhow!("Error fetching Meteora DAMM pool account"));
                }
            }
        }
    }

    if let Some(pools) = meteora_damm_v2_pools {
        for pool_address in pools {
            let meteora_damm_v2_pool_pubkey = Pubkey::from_str(pool_address)?;

            match rpc_client.get_account(&meteora_damm_v2_pool_pubkey) {
                Ok(account) => {
                    if account.owner != damm_v2_program_id() {
                        error!("Meteora DAMM V2 pool {} is not owned by the Meteora DAMM V2 program, skipping", pool_address);
                        continue;
                    }

                    let (mint_a, mint_b, vault_a, vault_b) =
                        get_dammv2_info(&account.data);

                    if mint_pubkey != mint_a && mint_pubkey != mint_b {
                        error!(
                            "Mint {} not found in meteora damm v2 pool {}",
                            mint_pubkey, pool_address
                        );
                        continue;
                    }

                    let (token_mint, base_mint, token_x_vault, token_sol_vault) =
                        if mint_pubkey == mint_a {
                            (mint_a, mint_b, vault_a, vault_b)
                        } else {
                            (mint_b, mint_a, vault_b, vault_a)
                        };

                    pool_data.add_meteora_damm_v2_pool(
                        pool_address,
                        &token_x_vault.to_string(),
                        &token_sol_vault.to_string(),
                        &token_mint.to_string(),
                        &base_mint.to_string(),
                    )?;
                }
                Err(e) => {
                    error!(
                        "Error fetching Meteora DAMM V2 pool account {}: {:?}",
                        meteora_damm_v2_pool_pubkey, e
                    );
                    continue;
                }
            }
        }
    }

    if let Some(pools) = solfi_pools {
        for pool_address in pools {
            let solfi_pool_pubkey = Pubkey::from_str(pool_address)?;

            match rpc_client.get_account(&solfi_pool_pubkey) {
                Ok(account) => {
                    if account.owner != solfi_program_id() {
                        error!(
                            "Solfi pool {} is not owned by the Solfi program, skipping",
                            pool_address
                        );
                        continue;
                    }

                    match SolfiInfo::load_checked(&account.data) {
                        Ok(solfi_info) => {
                            info!("Solfi pool added: {}", pool_address);
                            info!("    Base mint: {}", solfi_info.base_mint.to_string());
                            info!("    Quote mint: {}", solfi_info.quote_mint.to_string());
                            info!("    Base vault: {}", solfi_info.base_vault.to_string());
                            info!("    Quote vault: {}", solfi_info.quote_vault.to_string());

                            let token_x_vault = if sol_mint() == solfi_info.base_mint {
                                solfi_info.quote_vault
                            } else {
                                solfi_info.base_vault
                            };

                            let token_sol_vault = if sol_mint() == solfi_info.base_mint {
                                solfi_info.base_vault
                            } else {
                                solfi_info.quote_vault
                            };

                            // Determine token_mint and base_mint
                            let (token_mint, base_mint) = if mint_pubkey == solfi_info.base_mint {
                                (solfi_info.base_mint, solfi_info.quote_mint)
                            } else {
                                (solfi_info.quote_mint, solfi_info.base_mint)
                            };
                            
                            pool_data.add_solfi_pool(
                                pool_address,
                                &token_x_vault.to_string(),
                                &token_sol_vault.to_string(),
                                &token_mint.to_string(),
                                &base_mint.to_string(),
                            )?;
                        }
                        Err(e) => {
                            error!(
                                "Error parsing Solfi pool data from pool {}: {:?}",
                                pool_address, e
                            );
                            continue;
                        }
                    }
                }
                Err(e) => {
                    error!(
                        "Error fetching Solfi pool account {}: {:?}",
                        solfi_pool_pubkey, e
                    );
                    continue;
                }
            }
        }
    }

    if let Some(pools) = vertigo_pools {
        for pool_address in pools {
            let vertigo_pool_pubkey = Pubkey::from_str(pool_address)?;

            match rpc_client.get_account(&vertigo_pool_pubkey) {
                Ok(account) => {
                    if account.owner != vertigo_program_id() {
                        error!(
                            "Error: Vertigo pool account is not owned by the Vertigo program. Expected: {}, Actual: {}",
                            vertigo_program_id(), account.owner
                        );
                        return Err(anyhow::anyhow!(
                            "Vertigo pool account is not owned by the Vertigo program"
                        ));
                    }

                    match VertigoInfo::load_checked(&account.data, &vertigo_pool_pubkey) {
                        Ok(vertigo_info) => {
                            info!("Vertigo pool added: {}", pool_address);
                            info!("    Mint A: {}", vertigo_info.mint_a.to_string());
                            info!("    Mint B: {}", vertigo_info.mint_b.to_string());

                            let base_mint = pool_data.mint.to_string();

                            // Following the original loading pattern from user's code:
                            let non_base_vault = if base_mint == vertigo_info.mint_a.to_string() {
                                derive_vault_address(&vertigo_pool_pubkey, &vertigo_info.mint_b).0
                            } else {
                                derive_vault_address(&vertigo_pool_pubkey, &vertigo_info.mint_a).0
                            };
                            let base_vault = if base_mint == vertigo_info.mint_a.to_string() {
                                derive_vault_address(&vertigo_pool_pubkey, &vertigo_info.mint_a).0
                            } else {
                                derive_vault_address(&vertigo_pool_pubkey, &vertigo_info.mint_b).0
                            };

                            // Map to transaction expected fields:
                            // base_mint is our trading token, non-base should be SOL
                            let token_x_vault = base_vault; // vault for our trading token
                            let token_sol_vault = non_base_vault; // vault for SOL

                            info!("    Token X Vault: {}", token_x_vault.to_string());
                            info!("    Token SOL Vault: {}", token_sol_vault.to_string());
                            info!("");

                            // Determine token_mint and base_mint
                            let (token_mint, base_mint) = if mint_pubkey == vertigo_info.mint_a {
                                (vertigo_info.mint_a, vertigo_info.mint_b)
                            } else {
                                (vertigo_info.mint_b, vertigo_info.mint_a)
                            };
                            
                            pool_data.add_vertigo_pool(
                                pool_address,
                                &vertigo_info.pool.to_string(),
                                &token_x_vault.to_string(),
                                &token_sol_vault.to_string(),
                                &token_mint.to_string(),
                                &base_mint.to_string(),
                            )?;
                        }
                        Err(e) => {
                            error!(
                                "Error parsing Vertigo pool data from pool {}: {:?}",
                                vertigo_pool_pubkey, e
                            );
                            continue;
                        }
                    }
                }
                Err(e) => {
                    error!(
                        "Error fetching Vertigo pool account {}: {:?}",
                        vertigo_pool_pubkey, e
                    );
                    continue;
                }
            }
        }
    }

    Ok(pool_data)
}
