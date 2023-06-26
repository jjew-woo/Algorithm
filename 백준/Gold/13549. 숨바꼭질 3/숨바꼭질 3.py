from collections import deque

N, K = map(int, input().split())

if N >= K:
    print(N-K)
else:
    time = [0]*100001; visited = [False]*100001
    q = deque([])
    q.append(N)
    while q:
        n = q.popleft()
        visited[n] = True
        if n == K:
            print(time[n])
            break
        for i in (n*2, n-1, n+1):
            if 0 <= i < 100001 and not visited[i]:
                q.append(i)
                visited[i] = True
                if i == n*2:
                    time[i] = time[n]
                else:
                    time[i] = time[n]+1