# Day 4, Part 1

import lib

def main():
    # The grid is represented by a dict (x,y) -> '.'|'@'|'x'.
    # parse the grid
    grid , grid_num_rows, grid_num_cols = lib.parse()
    # print the grid
    lib.print_grid(grid, grid_num_rows, grid_num_cols)
    # new grid where the accessible locations are marked 'x'.
    new_grid = lib.mark_accessible(grid, grid_num_rows, grid_num_cols)
    # # print the new grid
    lib.print_grid(new_grid, grid_num_rows, grid_num_cols)
    count_x = sum(1 for v in new_grid.values() if v == 'x')
    print(f"Total 'x' marked: {count_x}")

if __name__ == "__main__":
    main()