from itertools import permutations

def change(op):
    o = ['+', '-', '*', '/']
    _op = []

    for i in range(4):
        if op[i]: _op += [o[i] for _ in range(op[i])]
    return _op

def cal(x, y, op):
    if op == '+':
        return x+y
    elif op == '-':
        return x-y
    elif op == '*':
        return x*y
    elif op == '/':
        if x < 0:
            return -(-(x)//y)
        return x//y

N = int(input())
number = list(map(int, input().split()))
operator = list(map(int, input().split()))
min_res = 1000000000; max_res = -1000000000

for case in set(permutations(change(operator), sum(operator))):
    res = number[0]
    for i in range(N-1):
        res = cal(res, number[i+1], case[i])
    
    min_res = min(min_res, res)
    max_res = max(max_res, res)

print(max_res)
print(min_res)