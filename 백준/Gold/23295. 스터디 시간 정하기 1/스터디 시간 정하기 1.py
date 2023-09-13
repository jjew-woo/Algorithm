N, T = map(int, input().split())
time = [0 for _ in range(100001)]; min_t =  100001; max_t = 0
for i in range(N):
    K = int(input())
    for _ in range(K):
        s, e = map(int, input().split())
        min_t = min(s, min_t); max_t = max(e, max_t)
        time[s] += 1; time[e] -= 1

for i in range(min_t, max_t+1):
    time[i] += time[i-1]

ans = [min_t, min_t+T]
rate = sum(time[min_t:min_t+T]); max_rate = rate
for i in range(min_t, max_t-T+1):
    rate -= time[i]
    rate += time[i+T]
    if rate > max_rate:
        max_rate = rate
        ans = [i+1, i+T+1]

print(ans[0], ans[1])