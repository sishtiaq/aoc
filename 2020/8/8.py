
import re
from input import test, actual

def parse(lines):
    pgm = []
    for line in lines:
        m = re.search('([a-z]+) ([-+0-9]+)', line)
        if m is not None:
            op = m.group(1)
            arg = int(m.group(2))
            pgm.append((op,arg))
    return pgm

def interp(pgm):
    acc = 0
    pc = 0
    go = True
    loop_check = 0
    addr_cache = set()
    
    while (go):
        if pc in addr_cache:
            print('pc={}, acc={}. already been here'.format(pc,acc))
            go = False
        addr_cache.add(pc)
        (op,arg) = pgm[pc]
        print('pc={}, acc={}, instr={}'.format(pc, acc, (op,arg)))
        if (op == 'acc'):
            acc = acc + arg
            pc = pc + 1
        elif (op == 'jmp'):
            pc = pc + arg
        elif (op == 'nop'):
            pc = pc + 1
        else:
            raise ValueError("bad instruction at pc {}".format(pc))


