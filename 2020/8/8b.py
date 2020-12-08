
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
    trace = []
    ret = True
    
    while (go):
        if (pc == len(pgm)):
            print('pc={}, acc={}. terminated ok'.format(pc,acc))
            ret = True
            break
        if pc in addr_cache:
            print('pc={}, acc={}. already been here'.format(pc,acc))
            ret = False
            break
        trace.append(pc) # trace pgm
        addr_cache.add(pc) # determine termination
        (op,arg) = pgm[pc]
#        print('pc={}, acc={}, instr={}'.format(pc, acc, (op,arg)))
        if (op == 'acc'):
            acc = acc + arg
            pc = pc + 1
        elif (op == 'jmp'):
            pc = pc + arg
        elif (op == 'nop'):
            pc = pc + 1
        else:
            raise ValueError("bad instruction at pc {}".format(pc))

    return (ret, acc, trace)

def replace(x):
    op,arg = x
    if op == 'nop':
        ret = ('jmp',arg)
    elif op == 'jmp':
        ret = ('nop',arg)
    else:
        ret = x
    return ret

def part2():
    pgm = parse(actual)
    ret, acc, trace = interp(pgm)
    count = 0
    
    for t in trace:
        print('*** replace instr {}'.format(t))
        pgm[t] = replace(pgm[t])
        ret2, acc2, trace2 = interp(pgm)
        print('ret={}, acc={}'.format(ret2,acc2))
        if ret2:
            print('count = {}'.format(count))
            break
        # un-replace
        pgm[t] = replace(pgm[t])
        count += 1
