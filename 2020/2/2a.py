
import functools

from input import input


def split(l):
    lohi, letter, s = l.split(' ')
    lo,hi = lohi.split('-')
    letter = letter.split(':')[0]
    return (int(lo),int(hi),letter,s)


def check(lo,hi,letter,string):
    c = string.count(letter)
    return (lo <= c and c <= hi)

if __name__ == "__main__":
    for i in input: 
        lo,hi,l,s = split(i)
        res = check(lo,hi,l,s)
        print('line is {}-{}, {}, s={}. check={}'.format(lo,hi,l,s,res))
