
import functools

from input import input

def split(l):
    lohi, letter, s = l.split(' ')
    lo,hi = lohi.split('-')
    letter = letter.split(':')[0]
    return (int(lo),int(hi),letter,s)


def check(lo,hi,letter,string):
    l1 = string[lo-1]
    l2 = string[hi-1]
    # either l1 or l2 is letter. 
    return ((l1 == letter and l2 != letter) or (l1 != letter and l2 == letter))

if __name__ == "__main__":
    for i in input: 
        lo,hi,l,s = split(i)
        res = check(lo,hi,l,s)
        print('line is {}-{}, {}, s={}. check={}'.format(lo,hi,l,s,res))
