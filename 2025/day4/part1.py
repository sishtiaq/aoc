# Day 4

def update_grid(grid, width, row, line): 
    for col in range(width):
        grid[(row, col)] = line[col]

def print_grid(grid, num_rows, num_cols):
    if not grid:
        print("D: (empty grid)")
        return
    # rows = [pos[0] for pos in grid.keys()]
    # cols = [pos[1] for pos in grid.keys()]
    # min_row, max_row = min(rows), max(rows)
    # min_col, max_col = min(cols), max(cols)
    min_row, max_row = 0, num_rows - 1
    min_col, max_col = 0, num_cols - 1
    for r in range(min_row, max_row + 1):
        line = ""
        for c in range(min_col, max_col + 1):
            line += grid.get((r, c), " ")
        print(line)

def mask(grid, num_rows, num_cols, row, col):
    mask = []
    # North
    if row > 0:
        mask += [(row-1, col)]
    # North-East
    if row > 0 and col < num_cols - 1:
        mask += [(row-1, col+1)]
    # East
    if col < num_cols - 1:
        mask += [(row, col+1)]
    # South East
    if row < num_rows - 1 and col < num_cols - 1:
        mask += [(row+1, col+1)]
    # South
    if row < num_rows - 1:
        mask += [(row+1, col)]
    # South West
    if row < num_rows - 1 and col > 0:
        mask += [(row+1, col-1)]
    # West
    if col > 0:
        mask += [(row, col-1)]
    # North West
    if row > 0 and col > 0:
        mask += [(row-1, col-1)]
    return mask

def apply_mask(grid, mask):
    values = []
    for pos in mask:
        if pos in grid:
            values += [grid[pos]]
    return values

def parse():
    pass
    
def main():
    grid = {}
    grid_num_rows = 0
    grid_num_cols = None
    # parse into grid
    while True:
        try:
            line = input()
            width = len(line)
            update_grid(grid, width, grid_num_rows, line)
            if grid_num_cols is None:
                grid_num_cols = width
            else: 
                assert(grid_num_cols == width)
            grid_num_rows += 1
        except EOFError:
            break
    # print the grid
    print_grid(grid, grid_num_rows, grid_num_cols)
    # apply mask to each cell
    new_grid = grid.copy()
#    xs = 0
    for r in range(grid_num_rows):
        for c in range(grid_num_cols):
            # only generate mask for '@' cells
            if grid.get((r, c), ' ') == '@':
                m = mask(grid, grid_num_rows, grid_num_cols, r, c)
                neighbours = apply_mask(grid, m)
                neighbours_papers = [n for n in neighbours if n == '@']
                if len(neighbours_papers) < 4:
                    new_grid[(r, c)] = 'x'
#                    xs += 1
                    print(f"D:  grid[{r}][{c}] has less than 4 paper neighbors.")
    # print the new grid
    print_grid(new_grid, grid_num_rows, grid_num_cols)
    count_x = sum(1 for v in new_grid.values() if v == 'x')
    print(f"Total 'x' marked: {count_x}")

if __name__ == "__main__":
    main()