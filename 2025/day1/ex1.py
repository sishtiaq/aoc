
def sum(cur_pos, dir, dist):
    assert(dir in ["L", "R"])
    if dir == "L":
        new_dist = 100 - dist 
        print(f"D: Replace L{dist} => R{new_dist}")
    else: # if dir == "R":    
        new_dist = dist
    # no L anymore, so only R/+.
    return (cur_pos + new_dist) % 100

import re
def parse(s):
    match = re.match(r"([LR])(\d+)", s)
    if match:
        dir = match.group(1)
        dist = int(match.group(2))
        return (dir, dist)
    else:
        raise ValueError("Invalid input format.")

def main():
    zeros = 0
    cur_pos = 50
    # read while not eof from stdin
    while True:
        try:
            #read line
            line = input()
            dir, dist = parse(line)
            next_pos = sum(cur_pos, dir, dist)
            print(f"D: {cur_pos} --{dir}{dist} --> {next_pos}")
            if next_pos == 0:
                zeros += 1
            cur_pos = next_pos
        except EOFError:
            break
        except ValueError as e:
            print(f"Error: {e}")
    print(f"Total zeros encountered: {zeros}")

if __name__ == "__main__":
    main()