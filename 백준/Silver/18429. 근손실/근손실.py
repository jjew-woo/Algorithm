from math import factorial
from itertools import permutations

N, K = map(int, input().split())
kit = list(map(int, input().split()))
ans = factorial(N)

for case in (permutations(kit, N)):
    weight = 500
    for w in case:
        weight += (w-K)
        if weight < 500:
            ans -= 1
            break

print(ans)