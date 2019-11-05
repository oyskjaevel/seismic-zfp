

def zslice_threadfunc(filename, t_range, buffer, data_start_bytes, zslice_first_block_offset,
                block_bytes, zslice_unit_in_block, unit_bytes, chunk_bytes):
    with open(filename, 'rb') as f:
        for block_num in t_range:
            f.seek(data_start_bytes + zslice_first_block_offset * block_bytes
                   + zslice_unit_in_block * unit_bytes
                   + block_num * chunk_bytes, 0)
            buffer[block_num * unit_bytes:(block_num + 1) * unit_bytes] = f.read(unit_bytes)

