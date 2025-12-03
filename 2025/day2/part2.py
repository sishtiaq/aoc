# Day 2, Part 1

def check_id(id):
    sid = str(id) # perf :(
    l = len(sid)
    half = l // 2
    # E i. (id[0:i] * repeats) == id
    # where repeats = len(id)/len(id[0:i])
    # At least 2-letter sw (so, start from 1), and min 2 repeats (so, until half+1).
    for i in range(1, half+1): 
        sw = sid[0:i]
        repeats = l // i
        if sw * repeats == sid:
            print(f"=> BAD ID {id}")
            return id
    # otherwise        
    return None

def check(lo, hi):
    print(f"D: Check {lo}-{hi}")
    bad_ids = []
    for i in range(lo, hi + 1):
        maybe_bad_id = check_id(i)
        if maybe_bad_id is not None:
            bad_ids += [maybe_bad_id]
    return bad_ids

import lib
def main():
    line = input()
    records = line.split(",")
    ranges = map (lambda r: lib.parse(r), records)
    sum_of_bad_ids = 0
    for (lo, hi) in ranges:
        bad_ids = check(lo, hi)
        sum_of_bad_ids += sum(bad_ids)
    print(f"Sum of bad IDs: {sum_of_bad_ids}")

if __name__ == "__main__":
    main()