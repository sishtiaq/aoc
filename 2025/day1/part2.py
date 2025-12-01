# Day 1, Part 2

# naive count up/down, counting zeros passed.
def tick(cur_pos, dir, tick):
    print(f"D: tick ( {cur_pos} --{dir}{tick}--> ?")
    assert(dir in ["L", "R"])
    zeros = 0
    current_pos = cur_pos
    current_tick = tick

    # Clearer if `if` is inside `for`. But gone for efficiency/abstraction instead. 
    if dir == "L":
        op = (lambda x: x - 1)
        fix = (lambda x: 99 if x == -1 else x)
    else: # if dir == "R":
        op = (lambda x: x + 1)
        fix = (lambda x: 0 if x == 100 else x)

    for _ in range(tick):
        current_pos = op(current_pos)
        current_pos = fix(current_pos)
        if current_pos == 0:
            zeros += 1
        print(f"D: tick={current_tick}, pos={current_pos}.")
    print(f"D:      ): {cur_pos} --{dir}{tick}--> {current_pos}. Went past {zeros} zeros.")
    return current_pos, zeros

import lib as lib
def main():
    zeros = 0
    cur_pos = 50
    # read while not eof from stdin
    while True:
        try:
            #read line
            line = input()
            dir, dist = lib.parse(line)
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