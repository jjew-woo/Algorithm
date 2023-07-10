N, K, B = map(int, input().split())
light = [True for _ in range(N+1)]
cnt = 0

for _ in range(B):
    num = int(input())
    light[num] = False
    if num < K+1:
        cnt += 1

min_cnt = cnt

for i in range(1, N-K+1):
    if not light[i]:
        cnt -= 1
    if not light[i+K]:
        cnt += 1
    min_cnt = min(cnt, min_cnt)

print(min_cnt)