N, L = map(int, input().split())
pool = sorted([list(map(int, input().split())) for _ in range(N)])

cnt = 0; cur = 0
for s, e in pool:
    cur = max(s, cur)
    while (cur < e):
        cnt += 1
        cur += L
print(cnt)