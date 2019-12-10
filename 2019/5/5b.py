
from enum import Enum

mem = [3,225,1,225,6,6,1100,1,238,225,104,0,2,218,57,224,101,-3828,224,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,26,25,224,1001,224,-650,224,4,224,1002,223,8,223,101,7,224,224,1,223,224,223,1102,44,37,225,1102,51,26,225,1102,70,94,225,1002,188,7,224,1001,224,-70,224,4,224,1002,223,8,223,1001,224,1,224,1,223,224,223,1101,86,70,225,1101,80,25,224,101,-105,224,224,4,224,102,8,223,223,101,1,224,224,1,224,223,223,101,6,91,224,1001,224,-92,224,4,224,102,8,223,223,101,6,224,224,1,224,223,223,1102,61,60,225,1001,139,81,224,101,-142,224,224,4,224,102,8,223,223,101,1,224,224,1,223,224,223,102,40,65,224,1001,224,-2800,224,4,224,1002,223,8,223,1001,224,3,224,1,224,223,223,1102,72,10,225,1101,71,21,225,1,62,192,224,1001,224,-47,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1101,76,87,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,108,226,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1107,677,226,224,102,2,223,223,1006,224,344,1001,223,1,223,7,226,677,224,1002,223,2,223,1005,224,359,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,374,101,1,223,223,108,677,677,224,102,2,223,223,1006,224,389,1001,223,1,223,107,677,226,224,102,2,223,223,1006,224,404,101,1,223,223,1108,677,226,224,102,2,223,223,1006,224,419,1001,223,1,223,1107,677,677,224,1002,223,2,223,1006,224,434,101,1,223,223,1007,677,677,224,102,2,223,223,1006,224,449,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,464,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,479,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,494,101,1,223,223,1008,226,677,224,1002,223,2,223,1005,224,509,1001,223,1,223,1007,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,8,226,226,224,102,2,223,223,1006,224,539,101,1,223,223,1108,226,226,224,1002,223,2,223,1006,224,554,101,1,223,223,107,226,226,224,1002,223,2,223,1005,224,569,1001,223,1,223,7,226,226,224,102,2,223,223,1005,224,584,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,599,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,614,1001,223,1,223,108,226,226,224,1002,223,2,223,1006,224,629,101,1,223,223,107,677,677,224,102,2,223,223,1005,224,644,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,659,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,674,1001,223,1,223,4,223,99,226]

class Op(Enum):
    add = 1
    mul = 2
    inp = 3
    out = 4
    jit = 5
    jif = 6
    lt = 7
    eq = 8
    stp = 99

class Mode(Enum):
    pos = 0
    imm = 1

# arity of op
def params_for_op(op):
    tbl = { Op.add: 3,
            Op.mul: 3,
            Op.inp: 1,
            Op.out: 1,
            Op.jit: 2,
            Op.jif: 2,
            Op.lt: 3,
            Op.eq: 3,
            Op.stp: 0 }
    return tbl[op]

def extend_pmodes_if_needed(op,current_pmodes):
    op_params = params_for_op(op)
    current_pmodes_len = len(current_pmodes)
    pmodes = current_pmodes.copy()
    if op_params > current_pmodes_len:
        extend_by = op_params - current_pmodes_len
        ext = [Mode.pos] * extend_by 
        pmodes.extend(ext)
    return pmodes

def parse_mode(n):
    if n == Mode.pos.value:
        r = Mode.pos
    elif n == Mode.imm.value:
        r = Mode.imm
    else:
        raise Exception('bad mode {}'.format(n))
    return r

def parse_op(n):
    tbl = { Op.add.value: Op.add,
            Op.mul.value: Op.mul,
            Op.inp.value: Op.inp,
            Op.out.value: Op.out,
            Op.jit.value: Op.jit,
            Op.jif.value: Op.jif,
            Op.lt.value:  Op.lt,
            Op.eq.value:  Op.eq, 
            Op.stp.value: Op.stp  }
    if n in tbl:
        return tbl[n]
    else:
        raise Exception('parse_op: invalid n {}'.format(n))

def parse_opcode(n):
    s = str(n)
    # parse 2-digit n[1:0] as opcode 
    s_op = int(s[-2:])
    op = parse_op(s_op)
    # parse remaining (at least 1?) digits as param modes
    params_rev = s[:-2]
    params = params_rev[::-1]
    modes = [ parse_mode(int(p)) for p in params ]
    # modes might need left-extending by 0, if op has more params. 
    modes_x = extend_pmodes_if_needed(op,modes)
    # got op and modes    
    return (op,modes_x)

def get_param_value(mem, mode, param):
    if mode == Mode.imm:
        r = param
    elif mode == Mode.pos:
        r = mem[param]
    else:
        raise Exception('bad mode {}'.format(mode))
    return r

def interp(m):
    pc = 0
    while True:
        poss_op = m[pc]
        #print('pc={},  poss_op {}'.format(pc,poss_op))
        (op,pmodes) = parse_opcode(poss_op)
        # F,D,X mixup
        if op == Op.stp:
            print('stop')
            return # stop 
        elif op == Op.add:
            # fetch three params
            p1 = m[pc+1]
            p2 = m[pc+2]
            mr = m[pc+3] # "will never be immediate"
            v1 = get_param_value(m, pmodes[0], p1)
            v2 = get_param_value(m, pmodes[1], p2)
            r = v1 + v2
            #print('{},{},{},{} = add.{} {},{} -> {}'.format(m[pc],m[pc+1],m[pc+2],m[pc+3],pmodes,v1,v2,r))
            m[mr] = r
            pc += 4
        elif op == Op.mul:
            # fetch three params
            p1 = m[pc+1]
            p2 = m[pc+2]
            mr = m[pc+3] # "will never be immediate"
            v1 = get_param_value(m, pmodes[0], p1)
            v2 = get_param_value(m, pmodes[1], p2)
            r = v1 * v2
            #print('{},{},{},{} = mul.{} {},{} -> {}'.format(m[pc],m[pc+1],m[pc+2],m[pc+3],pmodes,v1,v2,r))
            m[mr] = r
            pc += 4
        elif op == Op.inp:
            # fetch one param
            p1 = m[pc+1]
            #print('{},{} = inp.{} {}'.format(m[pc],m[pc+1],pmodes,p1))
            print('input> ')
            i = input()
            m[p1] = int(i)
            pc += 2
        elif op == Op.out:
            # fetch one param
            p1 = m[pc+1]
            v1 = get_param_value(m, pmodes[0], p1)
            #print('{},{} = out.{} {}'.format(m[pc],m[pc+1],pmodes,v1))
            print('output {}'.format(v1))
            pc += 2
        elif op == Op.jit:
            # fetch two params
            p1 = m[pc+1]
            p2 = m[pc+2]
            v1 = get_param_value(m, pmodes[0], p1)
            v2 = get_param_value(m, pmodes[1], p2)
            #print('{},{},{} = jit.{} {},{}'.format(m[pc],m[pc+1],m[pc+2],pmodes,v1,v2))
            if v1 != 0:
                pc = v2
            else:
                pc += 3
        elif op == Op.jif:
            # fetch two params
            p1 = m[pc+1]
            p2 = m[pc+2]
            v1 = get_param_value(m, pmodes[0], p1)
            v2 = get_param_value(m, pmodes[1], p2)
            #print('{},{},{} = jif.{} {},{}'.format(m[pc],m[pc+1],m[pc+2],pmodes,v1,v2))
            if v1 == 0:
                pc = v2
            else:
                pc += 3
        elif op == Op.lt:
            # fetch three params
            p1 = m[pc+1]
            p2 = m[pc+2]
            mr = m[pc+3]
            v1 = get_param_value(m, pmodes[0], p1)
            v2 = get_param_value(m, pmodes[1], p2)
            #print('{},{},{},{} = lt.{} {},{}'.format(m[pc],m[pc+1],m[pc+2],m[pc+3],pmodes,v1,v2))
            if v1 < v2:
                m[mr] = 1
            else: 
                m[mr] = 0
            pc += 4
        elif op == Op.eq:
            # fetch three params
            p1 = m[pc+1]
            p2 = m[pc+2]
            mr = m[pc+3]
            v1 = get_param_value(m, pmodes[0], p1)
            v2 = get_param_value(m, pmodes[1], p2)
            #print('{},{},{},{} = eq.{} {},{}'.format(m[pc],m[pc+1],m[pc+2],m[pc+3],pmodes,v1,v2))
            if v1 == v2:
                m[mr] = 1
            else: 
                m[mr] = 0
            pc += 4
        else:
            raise Exception('bad opcode: {}'.format(op))

testop = 1002