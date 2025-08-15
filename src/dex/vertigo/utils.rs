use solana_sdk::pubkey::Pubkey;

pub fn derive_vault_address(pool: &Pubkey, mint: &Pubkey) -> (Pubkey, u8) {
    Pubkey::find_program_address(&[b"vault", pool.as_ref(), mint.as_ref()], &crate::dex::vertigo::constants::vertigo_program_id())
}
