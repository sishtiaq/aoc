# Day 4, Part 2

import lib

def main():
    # The grid is represented by a dict (x,y) -> '.'|'@'|'x'.
    # parse the grid
    grid , grid_num_rows, grid_num_cols = lib.parse()

    count_of_removed = 0
    while True:
        new_grid = lib.mark_accessible(grid, grid_num_rows, grid_num_cols)
        count_x = sum(1 for v in new_grid.values() if v == 'x')
        print(f"About to rm {count_x} @s")
        if count_x > 0:
            for pos in new_grid:
                if new_grid[pos] == 'x':
                    new_grid[pos] = '.'
            grid = new_grid
            count_of_removed += count_x
            lib.print_grid(grid, grid_num_rows, grid_num_cols)
        else:
            # no more 'x' marked, exit loop
            break

    print(f"Final: {count_of_removed} '@'s removed.")

if __name__ == "__main__":
    main()