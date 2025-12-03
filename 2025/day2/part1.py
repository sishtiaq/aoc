# Day 2, Part 1

def check_id(id):
    sid = str(id) # perf :(
    l = len(sid)
    if l % 2 == 0: # repeats can only be even
        half = l // 2
        if sid[0:half] == sid[half:]:
            print(f"=> BAD ID {id}")
            return id
        else:
            return None
    else:
        return None
    
def check(lo, hi):
    print(f"D: Check {lo}-{hi}")
    bad_ids = []
    for i in range(lo, hi + 1):
        maybe_bad_id = check_id(i)
        if maybe_bad_id is not None:
            bad_ids += [maybe_bad_id]
    return bad_ids

def parse(s):
    (lo,hi) = s.split("-")
    return (int(lo), int(hi))

def main():
    line = input()
    records = line.split(",")
    ranges = map (lambda r: parse(r), records)
    sum_of_bad_ids = 0
    for (lo, hi) in ranges:
        bad_ids = check(lo, hi)
        sum_of_bad_ids += sum(bad_ids)
    print(f"Sum of bad IDs: {sum_of_bad_ids}")

if __name__ == "__main__":
    main()