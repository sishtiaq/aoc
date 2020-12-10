
from input import i0, i1, i3





def parse(ii):
    return set([ int(i) for i in ii ])

def update_diffs(d1, d2, d3, curr, nxt):
    diff = nxt - curr
    if diff == 1:
        d1 += 1
    if diff == 2:
        d2 += 1
    if diff == 3:
        d3 += 1
    return d1, d2, d3

def part1(ii):
    diff1, diff2, diff3 = 0, 0, 0
    current_adapter = 0
    arrange = []
    iis = set(ii)
    while (len(iis) != 0):
#        print(f'ii={iis}')        
        choices = set()
        for i in iis:
            if (i-1 == current_adapter or i-2 == current_adapter or i-3 == current_adapter):
                choices.add(i)
        choice = min(choices)
        diff1, diff2, diff3 = update_diffs(diff1, diff2, diff3, current_adapter,choice)
        print(f'current_adapter={current_adapter} => choices={choices}, so pick {choice}')
        arrange.append(choice)
        iis.remove(choice)
        current_adapter = choice
    diff3 += 1 # cos of last adapter-->device
    return diff1, diff2, diff3, arrange



class Tree:
    def __init__(self, d):
        self.data = d
        self.children = []

def dfs_wrapper(tree):
    acc = []    
    def dfs(tree, stack):
        stack = stack + [tree.data]
        if (len(tree.children) == 0):
            acc.append(stack)
        else:
            for c in tree.children:
                dfs(c, stack)

    dfs(tree, [])
    return acc

def mk_tree(current_adapter, tree, ii):
    choices = set()
    for i in ii:
        if (i-1 == current_adapter or i-2 == current_adapter or i-3 == current_adapter):
            choices.add(i)
    for choice in choices:
        child_tree = Tree(choice)
        ii_copy = ii.copy()
        ii_copy.remove(choice)
        mk_tree(choice, child_tree, ii_copy)
        tree.children.append(child_tree)
    return

def part2(input):
    t = Tree(0)
    mk_tree(0, t, parse(input))
    acc = dfs_wrapper(t)
    return acc
# nope

# def part2c(input):
#     input.sort()
#     input = input + [max(input) + 3]
#     ans = {}
#     ans[0] = 1
#     for i in i3:
#         ans[i] = ans.get(i-1,0) + ans.get(i-2,0) + ans.get(i-3,0)
#         print(f'ans[{i}] = {ans[i]} = {ans.get(i-1,0)} + {ans.get(i-2,0)} + {ans.get(i-3,0)}')
#     return ans
