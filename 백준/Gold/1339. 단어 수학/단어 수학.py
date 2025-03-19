import sys


N = int(sys.stdin.readline())
lst = [sys.stdin.readline().rstrip() for _ in range(N)]

maxlen = len(max(lst,key=len))
for i,t in enumerate(lst):
    lst[i] = t.zfill(maxlen)

num = 9
alpha = {}
for i in range(maxlen):
    for j, t in enumerate(lst):
        if t[i].isalpha():
            if t[i] not in alpha:
                alpha[t[i]] = pow(10, maxlen-i-1)
            else:
                alpha[t[i]] += pow(10, maxlen-i-1)
alpha = sorted(alpha.items(), key=lambda x: x[1], reverse=True)
answer = 0
for i, v in alpha:
    answer += v*num
    num-=1
print(answer)