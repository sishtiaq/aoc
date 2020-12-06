
from input import test,actual

def lex(input):
    # use empty line to put records together
    rr = []
    acc = ''
    for i in input:
        if i == '':
            rr.append(acc)
#            print('r is {}'.format(r))
            acc = ''
        else:
            acc = acc + ' ' + i
    # last acc
    rr.append(acc)
    
    # split records into list elts
    ss = []
    for r in rr:
        kvs = r.split(' ')
        ss.append(kvs)

    # rm pesky ''s
    tt = []
    for s in ss:
        s1 = list(filter (lambda x : x != '', s))
        tt.append(s1)
        
    return tt

# returns a list of (group_size, dict_of_questions_answered)
def count_dict(groups):
    cc = []
    for group in groups:
        c = {} # dict for group's questions/answered
        num_in_group = len(group)
        for person in group:
            # person is a string
            for q in person:
                if q not in c:
                    c[q] = 1
                else:
                    c[q] = c[q] + 1
        cc.append((num_in_group,c))
    return cc

def count(groups):
    acc = []
    for group in groups:
        group_size,dictionary = group
        total = 0
        for (k,v) in dictionary.items():
            if (v == group_size):
                total = total + 1
        acc.append(total)
    return acc

def ans(i):
    return sum(count(count_dict(lex(i))))

