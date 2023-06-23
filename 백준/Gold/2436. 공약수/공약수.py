from collections import defaultdict
from itertools import combinations

def factorization(x):
    l = defaultdict(int)
    d = 2
    while d <= x:
        if x % d == 0:
            l[d] += 1
            x = x / d
        else:
            d += 1
    return l

a, b = map(int, input().split())
f_a = factorization(a)
f_b = factorization(b)

mul = a
for i in f_b:
    f_b[i] -= f_a[i]
    mul *= (i**f_b[i])

min_a, min_b = b,b
for i in range(len(f_b)):
    for group in combinations(f_b.keys(), i):
        n1, n2 = a, mul
        for x in group:
            n1 *= (x**f_b[x])
            n2 //= (x**f_b[x])

        if n1+n2 < min_a+min_b:
            min_a, min_b = n1, n2

print(min_a, min_b) if min_a < min_b else print(min_b, min_a)