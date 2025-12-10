# Day 6, Part 1

def find_all(ss, elt):
    indices = set()
    start = 0
    for i,s in enumerate(ss):
        if s == elt:
            indices.add(i)
        start = i + 1
    return indices

def line_with_beams(line, beams):
    new_line = ''
    for i,c in enumerate(line):
        if i in beams:
            new_line += '|'
        else:
            new_line += c
    return new_line

def post_split_beams(beams):
    new_beams = set()
    for b in beams:
        new_beams.add(b - 1)
        new_beams.add(b + 1)
    return new_beams

def main():
    beams_so_far = set()
    row = 0
    total_beams_split_so_far = 0
    
    # 1st line tells us where S is
    line = input()
    idx_S = line.index('S')
    print(f"#0:{line} --- S@{idx_S}")
    beams_so_far.add(idx_S)

    # update beams_so_far for splitters '^' in each line
    while True:
        try:
            line = input()
            splitters = find_all(line, '^')
            beams_that_would_be_split = beams_so_far.intersection(splitters)
            split_beams = post_split_beams(beams_that_would_be_split)
            beams_so_far = beams_so_far.difference(beams_that_would_be_split)
            beams_so_far = beams_so_far.union(split_beams)
            # print debug calculations only
            count_beams_that_would_be_split = len(beams_that_would_be_split)
            total_beams_split_so_far += count_beams_that_would_be_split
            print(f"#{row}:{line_with_beams(line, beams_so_far)} --- split beams {count_beams_that_would_be_split}")
            row += 1
        except EOFError:
            break

    print(f"Total beams split: {total_beams_split_so_far}")

if __name__ == "__main__":
    main()