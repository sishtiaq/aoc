# Day 1, Part 2

# naive count up/down, counting zeros passed.
def tick(cur_pos, dir, tick):
    print(f"D: tick ( {cur_pos} --{dir}{tick}--> ?")
    assert(dir in ["L", "R"])
    zeros = 0
    current_pos = cur_pos
    current_tick = tick
    # TODO: pull if out of for. 
    for _ in range(tick):
        if dir == "L":
            current_pos = (current_pos - 1)
            if current_pos == -1:
                current_pos = 99
        else: # if dir == "R":
            current_pos = (current_pos + 1)
            if current_pos == 100:
                current_pos = 0
        if current_pos == 0:
            zeros += 1
        print(f"D: tick={current_tick}, pos={current_pos}.")
    print(f"D:      ): {cur_pos} --{dir}{tick}--> {current_pos}. Went past {zeros} zeros.")
    return current_pos, zeros

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
            next_pos, zeros_in_this_tick = tick(cur_pos, dir, dist)
            cur_pos = next_pos
            zeros += zeros_in_this_tick
        except EOFError:
            break
        except ValueError as e:
            print(f"Error: {e}")
    print(f"Total zeros encountered: {zeros}")

if __name__ == "__main__":
    main()