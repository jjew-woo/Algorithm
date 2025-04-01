from itertools import combinations

N = int(input())
strength = list(map(int, input().split()))
pleasure = list(map(int, input().split()))

m = 0

for n in range(1,N+1):
    for c in combinations(list(range(N)), n):
        s = 0; p = 0
        for i in c:
            s += strength[i]
            p += pleasure[i]
                
        if s < 100 and p > m:
            m = p

print(m)