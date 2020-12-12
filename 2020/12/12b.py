
import math
from input import t0, t1

# hard-code sin, cos for 90,180,270,360
sin = {90:1, 180:0, 270:-1, 360:0}
cos = {90:0, 180:-1, 270:0, 360:1}

def rotate_waypoint(x, y, direction, angle):
    if direction == 'L':
        th = angle
    else:
        th = 360 - angle

    new_x = (cos[th] * x) - (sin[th] * y)
    new_y = (sin[th] * x) + (cos[th] * y)
    return new_x,new_y

def run(instrs):
    s_x,s_y = 0,0 # ship
    w_x,w_y = 10,1# waypoint (relative to ship)
    for (a,v) in instrs:
        if a == 'N':
            w_y += v
        elif a == 'S':
            w_y -= v
        elif a == 'E':
            w_x += v
        elif a == 'W':
            w_x -= v
        elif a == 'L' or a == 'R':
            w_x,w_y = rotate_waypoint(w_x, w_y, a, v)
        elif a == 'F':
            s_x, s_y = s_x + (v * w_x), s_y + (v * w_y)
        else:
            msg = 'bad action (' + a + ',' + string(v) + ')'
            raise ValueError(msg)
        print(f'{a}{v:02} --> ({s_x},{s_y}), ({w_x},{w_y})')


def part2(instrs):
    run(instrs)
