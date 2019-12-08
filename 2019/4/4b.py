from re import finditer
from re import search

# C1: a 6-digit number is represented as a 6-tuple
#     d6 = (x5,x4,x3,x2,x1,x0)
#  Easier to check C3, C4 if uses this representation. 

# C2: within {min, max} values
def check_range(min, max, n):
    return (n>= min and n<=max)

# C3: two adjacents digits are the same
def two_adj_same(d6):
    (d5,d4,d3,d2,d1,d0) = d6
    eq54 = (d5 == d4)
    eq43 = (d4 == d3)
    eq32 = (d3 == d2)
    eq21 = (d2 == d1)
    eq10 = (d1 == d0)
    return (eq54 or eq43 or eq32 or eq21 or eq10)

def has_exact_double(password):
    return any(len(match.group(0)) == 2 for match in finditer(r'(\d)\1+', password))

# C4: going from left to right, digits never decrease 
# only increase or stay the same
def digits_dont_decrease(d6):
    (d5,d4,d3,d2,d1,d0) = d6
    c54 = (d5 <= d4)
    c43 = (d4 <= d3)
    c32 = (d3 <= d2)
    c21 = (d2 <= d1)
    c10 = (d1 <= d0)
    return (c54 and c43 and c32 and c21 and c10)

# all-predicate
def check(min,max,n6):
    d6 = str(n6)
    p = check_range(min,max,n6) and two_adj_same(d6) and digits_dont_decrease(d6)
    return p

def check2(min,max,n6):
    d6 = str(n6)
    p = check_range(min,max,n6) and has_exact_double(str(n6)) and digits_dont_decrease(d6)
    return p

# generate all valid pswds
def gen(min,max):
    xx = [ x for x in range(min,max+1)
                if check2(min,max,x) ]
    return xx

min = 172851
max = 675869

# test cases
# x1 = (1,1,1,1,1,1)
# x2 = (2,2,3,4,5,0)
# x3 = (1,2,3,7,8,9)