use solana_sdk::pubkey::Pubkey;

pub fn update_tick_array_accounts_for_onchain(
    whirlpool: &Pubkey,
    tick_arrays: &mut Vec<Pubkey>,
    a_to_b: bool,
    tick_spacing: u16,
    tick_current_index: i32,
) {
    let mut tick_array_offset = 0;
    let tick_array_count = tick_arrays.len();

    if a_to_b {
        // A to B
        if tick_array_count == 1 {
            tick_array_offset = 1;
        } else if tick_array_count == 2 {
            tick_array_offset = 1;
        }
    } else {
        // B to A
        if tick_array_count == 1 {
            tick_array_offset = -1;
        } else if tick_array_count == 2 {
            tick_array_offset = -1;
        }
    }

    let tick_array_start_index = tick_current_index as i32
        - (tick_current_index as i32
            % (tick_spacing as i32 * crate::dex::whirlpool::state::TICK_ARRAY_SIZE as i32))
        + tick_array_offset * tick_spacing as i32 * crate::dex::whirlpool::state::TICK_ARRAY_SIZE as i32;

    let (tick_array_pubkey, _) = Pubkey::find_program_address(
        &[
            b"tick_array",
            whirlpool.as_ref(),
            &tick_array_start_index.to_le_bytes(),
        ],
        &crate::dex::whirlpool::constants::whirlpool_program_id(),
    );

    if !tick_arrays.contains(&tick_array_pubkey) {
        tick_arrays.push(tick_array_pubkey);
    }
}
