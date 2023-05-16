import bitcoin_explorer as bex


### Database ###
db = bex.BitcoinDB("D:/Coding/Bitcoin/Data", False)

### Functions ###
def get_difficulty(blockindex):
    if blockindex < 0:
        return None

    n_bits = db.get_block_header(blockindex)['block_header']['bits']
    n_shift = (n_bits >> 24) & 0xff
    d_diff = (float)(0x0000ffff) / (float)(n_bits & 0x00ffffff)

    while n_shift < 29:
        d_diff *= 256.0
        n_shift += 1
    while n_shift > 29:
        d_diff /= 256.0
        n_shift -= 1

    return d_diff

def get_time(blockindex):
    if blockindex < 0:
        return None

    time = int(db.get_block_header(blockindex)['block_header']['time'])
    return time

def average_block_paces_epoch(difficulty_times):
    block_paces = []
    times = []

    for i in range(2016):
        height = difficulty_times * 2016 + i
        time = int(db.get_block_header(height)['block_header']['time'])
        times.append(time)

    for i in range(len(times) - 1):
        time1 = times[i+1]
        time2 = times[i]
        block_paces.append((time1 - time2)/60.0)

    return sum(block_paces) / len(block_paces)