import re

def parse(str):
    m = re.search(r'(\w+)\)(\w+)',str)
    x,y = m.group(1), m.group(2)
    return (x,y)

def mkOrbitsDict(fname):
    orbits = {}
    f = open(fname,'r')
    for l in f:
        (x,y) = parse(l)
        orbits[y] = x 
    return orbits

fname = 'input'
orbits = mkOrbitsDict(fname)
planets = set(orbits.keys())

all_l = 0
for p in planets:
    cursor = p
    l = 0
    path = [p]
    while cursor != 'COM':
        # o ) p
        o = orbits[cursor]
        path.append(o)
        l += 1
        cursor = o
    print('planet {}: path={}, len={}'.format(p,path,l))
    all_l += l

