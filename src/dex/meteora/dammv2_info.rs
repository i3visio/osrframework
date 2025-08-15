use anyhow::Result;
use solana_program::pubkey::Pubkey;

pub fn get_dammv2_info(data: &[u8]) -> (Pubkey, Pubkey, Pubkey, Pubkey) {
    if data.len() < 296 {
        panic!("Invalid data length for DAMMv2 info");
    }

    (
        Pubkey::new_from_array(data[168..200].try_into().unwrap()),
        Pubkey::new_from_array(data[200..232].try_into().unwrap()),
        Pubkey::new_from_array(data[232..264].try_into().unwrap()),
        Pubkey::new_from_array(data[264..296].try_into().unwrap()),
    )
}
