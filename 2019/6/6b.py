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
def paths_to_root(fname):
    orbits = mkOrbitsDict(fname)
    planets = set(orbits.keys())
    planet_data = {}

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
        planet_data[p] = (path,l)
        all_l += l
    print('total path lens={}'.format(all_l))
    return planet_data

# find first common parent b/t YOU and SAN.
pp = paths_to_root(fname)
you = pp['YOU'][0]
san = pp['SAN'][0]
you.reverse()
san.reverse()
common_parent = 0
while (you[common_parent] == san[common_parent]):
    common_parent += 1
common_parent -= 1 # 'cos index from 0
# len of you[i]->you.index(YOU)
# -2 'cos we don't count you[i] and YOU. 
len_you = len(you) - you.index(you[common_parent]) - 2
len_san = len(san) - san.index(san[common_parent]) - 2