
from input import t0, t1, test0

def border(grid,x,y):
    return x == -1 or x == len(grid) or y == -1 or y == len(grid[0])

def get(grid, x, y):
    if not border(grid,x,y):
        d = grid[x][y]
    else:
        d = 0
    return d

def pr(grid):
    for x in grid:
        print(f'{x}')

# part 1
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

# part 2
incr_tbl = { 'NW':(-1,-1), 'N':(-1,0), 'NE':(-1,+1),
             'W': (0,-1), 'E':(0,+1),
             'SW': (+1,-1), 'S':(+1,0), 'SE':(+1,+1) }

def view(grid, xy):
    x,y = xy
    seen = []
    for dir in ['NW','N','NE','W','E','SW','S','SE']:
        cursor_x,cursor_y = x,y
        while not border(grid, cursor_x, cursor_y):
            incr_x,incr_y = incr_tbl[dir]
            cursor_x = cursor_x + incr_x
            cursor_y = cursor_y + incr_y
            d = get(grid,cursor_x,cursor_y)
            if d == 'L' or d == '#':
                seen.append(d)
                break
    return ''.join(seen).count('#')

def iter2(grid):
    new_grid = grid.copy()
    for idx,x in enumerate(grid):
        for idy,y in enumerate(x):
            if grid[idx][idy] == 'L' and view(grid,(idx,idy))==0:
                new_grid[idx] = new_grid[idx][:idy] + '#' + new_grid[idx][idy+1:]
            elif grid[idx][idy] == '#' and view(grid,(idx,idy))>=5:
                new_grid[idx] = new_grid[idx][:idy] + 'L' + new_grid[idx][idy+1:]
            else:
                z = 42
    return new_grid

# find iterf(iterf(...(g)...))
def fx(g,iterf):
    grid = g
    flag = True
    round = 1
    while (flag):
        next_grid = iterf(grid)
        if next_grid == grid:
            flag = False
        round += 1
        grid = next_grid.copy()
        # leaking old grid
    print(f'fx after {round} rounds')
    return grid

def part1(g):
    fixed_g = fx(g,iter)
    return ''.join(fixed_g).count('#')

def part2(g):
    fixed_g = fx(g,iter2)
    return ''.join(fixed_g).count('#')
