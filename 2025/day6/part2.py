# Day 6, Part 1

initial = {
    "+": 0,
    "*": 1
}

def parse_op_op(op):
    if op == "+":
        return ("+",lambda x, y: x + y)
    elif op == "*":
        return ("*",lambda x, y: x * y)
    else:
        return (" ", lambda x, y: 0)
        raise Exception(f"Unknown op {op}")
    
import functools

def main():
    max_row = 0
    max_col = 0 
    grid = {}
    operator = {}

    # parse
    while True:
        try:
            line = input()
            if line[0] in ['*','+']:
                for i,c in enumerate(line):
                    if c in ['*','+']:
                        operator[i] = (i, c) #ßparse_op_op(c))
                    
            else:
                for i,c in enumerate(line):
                    # print(f"char[{i}]: {c}")
                    grid[(max_row, i)] = c
                    
            max_col = max(max_col, len(line))
            max_row += 1
        except EOFError:
            break

    # grid transpose to parse columns.
    gridt = {}
    for c in range(max_col):
        n = []
        for r in range(max_row):
            n.append(grid.get((r,c),'-'))
        gridt[c] = ''.join(filter(lambda x: x != '-', n))

    set_of_cols = {}
    current_col = []
    current_start_idx = 0
    started = True
    for k,v, in gridt.items():
        # print(f"gridt[{k}] = '{v}' (len={len(v)})")
        if gridt[k].strip().isdigit():
            current_col.append(int(gridt[k]))
        else:
            set_of_cols[current_start_idx] = current_col
            current_start_idx = k + 1
            current_col = []
    set_of_cols[current_start_idx] = current_col

    total = 0
    for k,v in operator.items():
        (pos, op) = v
        f = parse_op_op(op)
        sum = functools.reduce(f[1], set_of_cols.get(k, []), initial[op])
        print(f"sum[{k}] = {sum}")
        total += sum

    print(f"total={total}")

if __name__ == "__main__":
    main()