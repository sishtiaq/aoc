
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
    print("D: End of grid")

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

def conv(grid, mask):
    values = []
    for pos in mask:
        if pos in grid:
            values += [grid[pos]]
    return values

def parse():
    grid = {}
    grid_num_rows = 0
    grid_num_cols = None
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
    return (grid, grid_num_rows, grid_num_cols)

def mark_accessible(grid, num_rows, num_cols):  
    new_grid = grid.copy()
    for r in range(num_rows):
        for c in range(num_cols):
            # only generate mask for '@' cells
            if grid.get((r, c), ' ') == '@':
                m = mask(grid, num_rows, num_cols, r, c)
                neighbours = conv(grid, m)
                paper_neighbours = [n for n in neighbours if n == '@']
                if len(paper_neighbours) < 4:
                    new_grid[(r, c)] = 'x'
#                    print(f"D:  grid[{r}][{c}] has less than 4 paper neighbors.")
    return new_grid