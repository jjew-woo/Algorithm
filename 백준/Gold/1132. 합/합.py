from collections import defaultdict

ans = 0
N = int(input())
alpha = defaultdict(int)
first = set()

for _ in range(N):
    s = input()
    l = len(s)
    for i in range(l):
        if i == 0:
            first.add(s[i])
        alpha[s[i]] += (10**(l-i-1))

k = len(alpha)
i = 1 if k == 10 else 10-k
zero = (k>9)
for c, sum in sorted(alpha.items(), key=lambda item:item[1]):
    if zero and c not in first:
        zero = False
    else:
        ans += (sum*i)
        i += 1

print(ans)