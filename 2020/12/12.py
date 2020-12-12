
from input import t0, t1

# "R90 would cause the ship to turn right by 90 degrees"
# but in the test case, the ship E,R90 -> S ?!
def new_dir(cur_dir, direction, angle):
    if direction == 'R': 
        new_dir = (cur_dir - angle) % 360
    else:
        new_dir = (cur_dir + angle) % 360
    return new_dir

def fwd(cur_dir, x, y, v):
    # cheating, knowing that cur_dir \in {(0),90,180,270)
    if cur_dir == 0:
        return x,y+v
    if cur_dir == 90:
        return x-v,y
    if cur_dir == 180:
        return x,y-v
    if cur_dir == 270:
        return x+v,y
    raise ValueError('bad assumption about dir')

def final_msg(x, y, d):
    l = 'east'
    u = 'north'
    if x < 0:
        l = 'west'
    if y < 0:
        u = 'south'
    print(f'final position: ({l} {abs(x)}, {u} {abs(y)}) facing {d}')
    
def run(instrs):
    direction = 270
    pos_x,pos_y = 0,0
    for (a,v) in instrs:
        if a == 'N':
            pos_y += v
        elif a == 'S':
            pos_y -= v
        elif a == 'E':
            pos_x += v
        elif a == 'W':
            pos_x -= v
        elif a == 'L' or a == 'R':
            direction = new_dir(direction, a, v)
        elif a == 'F':
            pos_x, pos_y = fwd(direction, pos_x, pos_y, v)
        else:
            msg = 'bad action (' + a + ',' + string(v) + ')'
            raise ValueError(msg)
        print(f'{a}{v} --> east {pos_x}, north {pos_y}, dir={direction}')

    final_msg(pos_x,pos_y,direction)
