
from input import t0, t1

def border(grid,x,y):
    return x == -1 or x == len(grid) or y == -1 or y == len(grid[0])

def get(grid, x, y):
    if not border(grid,x,y):
        d = grid[x][y]
    else:
        d = 0
    return d


def adj(grid, xy):
    max_x = len(grid) - 1
    max_y = len(grid[0]) - 1
    x,y = xy

    ad = []
    tl = get(grid, x-1,y-1)
    ad.append(tl)
    t = get(grid, x-1,y)
    ad.append(t)
    tr = get(grid, x-1,y+1)
    ad.append(tr)
    l = get(grid, x,y-1)
    ad.append(l)    
    r = get(grid, x,y+1)
    ad.append(r)    
    bl = get(grid, x+1,y-1)
    ad.append(bl)
    b = get(grid, x+1, y)
    ad.append(b)    
    br = get(grid, x+1, y+1)
    ad.append(br)    
#    print(f'{tl}{t}{tr}\n{l}-{r}\n{bl}{b}{br}')
    return ad.count('#')

def pr(grid):
    for x in grid:
        print(f'{x}')

def iter(grid):
    new_grid = grid.copy()
    for idx,x in enumerate(grid):
        for idy,y in enumerate(x):
            if grid[idx][idy] == 'L' and adj(grid,(idx,idy))==0:
#                print(f'update {idx}{idy} L->#')
                new_grid[idx] = new_grid[idx][:idy] + '#' + new_grid[idx][idy+1:]
            elif grid[idx][idy] == '#' and adj(grid,(idx,idy))>=4:
                new_grid[idx] = new_grid[idx][:idy] + 'L' + new_grid[idx][idy+1:]
#                print(f'update {idx}{idy} #->L')
            else:
                z = 42
#                print(f'noupdat {idx}{idy} {grid[idx][idy]}')
    return new_grid

def fx(g):
    grid = g
    flag = True
    round = 1
    while (flag):
        next_grid = iter(grid)
        if next_grid == grid:
            flag = False
        round += 1
        grid = next_grid.copy()
        # leaking old grid
    print(f'fx after {round} rounds')
    return grid

def part1(g):
    fixed_g = fx(g)
    return ''.join(fixed_g).count('#')
