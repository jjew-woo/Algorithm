import re

T = int(input())

for _ in range(T):
    n = input()
    p = re.compile('(100+1+|01)+')
    if p.fullmatch(n):
        print("YES")
    else:
        print("NO")