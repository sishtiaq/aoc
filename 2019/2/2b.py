
from enum import Enum

class Op(Enum):
    add = 1
    mul = 2
    stp = 99
    
    
def add(m, m1,m2):
    return m[m1] + m[m2]

def mul(m, m1, m2):
    return m[m1] * m[m2]

def stop(m):
    return 


def interp(m):
    pc = 0
    while True:
        if m[pc] == Op.stp.value:
            #print('stop')
            # final
            #print(m)
            return
        else:
            # fetch 
            op = m[pc]
            m1 = m[pc+1]
            m2 = m[pc+2]
            mr = m[pc+3]
            # print('({},{},{},{})'.format(op,m1,m2,mr))
            # exec 
            if op == Op.add.value:
                r = add(m,m1,m2)
            elif op == Op.mul.value:
                r = mul(m,m1,m2)
            else:
                # error
                return
            # WB
            m[mr] = r
        pc += 4

def main():

    mem_init = [ 1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,2,9,19,23,1,23,6,27,1,13,27,31,1,31,10,35,1,9,35,39,1,39,9,43,2,6,43,47,1,47,5,51,2,10,51,55,1,6,55,59,2,13,59,63,2,13,63,67,1,6,67,71,1,71,5,75,2,75,6,79,1,5,79,83,1,83,6,87,2,10,87,91,1,9,91,95,1,6,95,99,1,99,6,103,2,103,9,107,2,107,10,111,1,5,111,115,1,115,6,119,2,6,119,123,1,10,123,127,1,127,5,131,1,131,2,135,1,135,5,0,99,2,0,14,0 ]

    for noun in range(0,100):
        for verb in range(0,100):
            mem = mem_init.copy()
            mem[1] = noun
            mem[2] = verb
            interp(mem)
            if mem[0] == 19690720:
                print('v={}, n={}'.format(verb,noun))
                return
           
    

if __name__ == "__main__":
    main()
