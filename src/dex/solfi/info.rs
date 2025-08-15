use anyhow::Result;
use solana_sdk::pubkey::Pubkey;

pub struct SolfiInfo {
    pub base_mint: Pubkey,
    pub quote_mint: Pubkey,
    pub base_vault: Pubkey,
    pub quote_vault: Pubkey,
}

impl SolfiInfo {
    pub fn load_checked(data: &[u8]) -> Result<Self> {
        let (base_mint, quote_mint, base_vault, quote_vault) = load_pubkeys(data);

        Ok(Self {
            base_mint,
            quote_mint,
            base_vault,
            quote_vault,
        })
    }
}

fn load_pubkeys(data: &[u8]) -> (Pubkey, Pubkey, Pubkey, Pubkey) {
    (
        Pubkey::new_from_array(data[2664..2696].try_into().unwrap()),
        Pubkey::new_from_array(data[2696..2728].try_into().unwrap()),
        Pubkey::new_from_array(data[2736..2768].try_into().unwrap()),
        Pubkey::new_from_array(data[2768..2800].try_into().unwrap()),
    )
}
