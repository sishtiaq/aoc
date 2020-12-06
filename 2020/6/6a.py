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

def count_dict(groups):
    cc = []
    for group in groups:
        c = {} # dict for letters per group 
        for person in group:
            # person is a string
            for q in person:
                if q not in c:
                    c[q] = 1
                else:
                    c[q] = c[q] + 1
#        print('group {} has dict {}'.format(group,c))
        cc.append(c)
    return cc

def count(keys):
    return sum(list(map(len, keys)))

def ans(i):
    return count(count_dict(lex(i)))
