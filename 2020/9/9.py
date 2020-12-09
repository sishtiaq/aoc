
import itertools
from input import test0, test, actual

def dbg(s, debug):
    if debug:
        print(s)

def mk_sums(nn):
    return list(itertools.combinations(nn,2))

# this works too. mk_sums is faster (though I then list it). 
def matrix(nn):
    m = []
    for i in nn:
        for j in nn:
            if (i != j):
                m.append((i,j))
    return m

def check_valid(s, x):
    for (i,j) in s:
        if ((i+j) == x):
            return True
    return False

def find_nonsum(preamble_len, dd, debug=False):
    preamble_idx = 0
    nn = dd[preamble_len:]

    for n in nn:
        preamble = dd[preamble_idx:(preamble_len+preamble_idx)]
        dbg(f'preamble={preamble}', debug)
        sums = mk_sums(preamble)
        dbg(f'sums={sums}', debug)
        valid = check_valid(sums, n)
        dbg(f'{n} valid? {valid}', debug)
        if (not valid):
            print(f'{n} valid? {valid}')
            return n
        preamble_idx += 1
    return None

def find_sums(dd, total, debug=False):        
    for i in range(0,len(dd)):
        for j in range(0,len(dd)):
            if (sum(dd[i:j]) == total):
                return (min(dd[i:j]) + max(dd[i:j]))
    return None


def part1():
    return find_nonsum(25, actual)

def part2():
    s = find_nonsum(25, actual)
    return find_sums(actual, s)


    
