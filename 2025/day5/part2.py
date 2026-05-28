# Day 5, Part 1

def within(interval, intervals):
    (lo,hi) = interval
    for (exist_lo, exist_hi) in intervals:
        if exist_lo <= lo and hi <= exist_hi:
            print(f"\t=> Skip [{lo}-{hi}], within existing [{exist_lo}-{exist_hi}]")
            return True
    return False

def overlaps(interval, existing_interval):
    (lo, hi) = interval
    (exist_lo, exist_hi) = existing_interval
    if (exist_lo <= lo and lo <= exist_hi and hi > exist_hi) or \
        (lo <= exist_lo and exist_lo <= hi and hi <= exist_hi):
        return True
    else:
        return False
    
def find_overlap(interval, intervals):
    overlapping_intervals = set()
    (lo,hi) = interval
    for interval in intervals:
        if overlaps((lo, hi), interval):
            overlapping_intervals.add(interval)
    return overlapping_intervals

def calc_diff(interval, existing_interval):
    (lo,hi) = interval
    (exist_lo, exist_hi) = existing_interval
    if lo < exist_lo:
        return (lo, exist_lo - 1)
    else:
        return (exist_hi + 1, hi)
    
def separate(interval, intervals):
    (lo,hi) = interval
    for (exist_lo, exist_hi) in intervals:
        if exist_lo <= lo and hi <= exist_hi:
            print(f"\t=> Skip [{lo}-{hi}], within existing [{exist_lo}-{exist_hi}]")
            return False
    return True

def main():
    ranges = set()
    i = 1
    while True:
        try:
            line = input()
            if line == "":
                break
            else:
                # process fresh range input
                (x,y) = line.split("-")
                (lo,hi) = (int(x),int(y))
                print(f"#{i} Processing [{lo}-{hi}]")

                if within((lo,hi), ranges):
                    print(f"\t Skip, already got.")
                    continue
                else: # overlap, or new.
                    existing_range = find_overlap((lo,hi), ranges)
                    if len(existing_range) > 0:
                        # take away existing_range, add the larger overlap. 
                        new_range = existing_range.copy()
                        new_range.add((lo,hi))
                        min_lo = min(r[0] for r in new_range)
                        max_hi = max(r[1] for r in new_range)
                        print(f"\tOverlaps with existing ranges {sorted(list(existing_range))}, so add [{min_lo}-{max_hi}] only")
                        for r in existing_range:
                            ranges.remove(r)
                        ranges.add((min_lo, max_hi))
                    elif separate((lo,hi), ranges):
                        # new range, add as is.
                        print(f"\tNew, so Add [{lo}-{hi}]")
                        ranges.add((lo,hi))
                    else:
                        print(f"\tNeither within existing, overlap, or separate. So what is it [{lo}-{hi}]")
                        raise Exception("Unexpected range case")
        except EOFError:
            break
        i += 1

    num_of_ingredients = sum(hi - lo + 1 for (lo,hi) in ranges)
    print(f"Fresh Ingredients: {sorted(list(ranges))} Total: {num_of_ingredients}")

if __name__ == "__main__":
    main()