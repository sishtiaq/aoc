

min_rows, max_rows = 0, 127
min_cols, max_cols = 0, 7


import math

# re-use code for both row and col. 
def partition(spec, min_val, max_val):
    lo = min_val
    hi = max_val
    for s in spec:
        mid = math.floor((hi-lo)/2) + lo
        # lower half
        if (s == 'F' or s == 'L'):
            hi = mid
        # upper half
        elif (s == 'B' or s == 'R'):
            lo = mid + 1
        else:
            raise ValueError("invalid r")
#        print('{}, mid={}, ==> ({},{})'.format(s,mid,lo,hi))
    if (lo == hi):
        return lo
    else:
        raise ValueError("lo!=hi")

def score(x):
    (r,c) = x
    return r*8 + c

def day5(bp):
    row_spec = bp[0:7]
    col_spec = bp[7:]
    row = partition(row_spec, min_rows, max_rows)
    col = partition(col_spec, min_cols, max_cols)
    return (row,col)


from input import actual
rc = list(map(day5, actual))
ss = list(map(score, rc))
ans = max(ss)

