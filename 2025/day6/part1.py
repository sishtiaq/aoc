# Day 6, Part 1

initial = {
    "+": 0,
    "*": 1
}
def parse_num(numbers, cols):
    nn = [int(n) for n in numbers]
    col = 0
    for n in nn:
        cols[col].append(n) if col in cols else cols.update({col:[n]})
        col += 1

def parse_op_op(op):
    if op == "+":
        return ("+",lambda x, y: x + y)
    elif op == "*":
        return ("*",lambda x, y: x * y)
    else:
        raise Exception(f"Unknown op {op}")

def parse_op(ops, row):
    print(f"#{row} parse_op: {ops}")
    return [parse_op_op(op) for op in ops]

import functools

def main():
    cols = {}
    ops = {}
    row = 0

    while True:
        try:
            line = input()
            items = line.split()
            if (items[0].isdigit()):
                parse_num(items, cols)
                print(f"cols = {cols}")
            else:
                ops = parse_op(items, row)
                print(f"ops = {ops}")
            row += 1
        except EOFError:
            break

    total = 0
    for i, col in enumerate(cols):
        sum = functools.reduce(ops[i][1], cols[i], initial[ops[i][0]])
        print(f"#{i} fold {ops[i][0]} to {cols[i]} with base {initial[ops[i][0]]} = {sum}")
        total += sum

    print(f"Total: {total}")

if __name__ == "__main__":
    main()