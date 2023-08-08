from collections import deque

N = int(input()); M = int(input())

info = [[] for _ in range(N+1)]
for i in range(1,N+1):
    s = list(map(int, input().split()))
    for j in range(N):
        if s[j]:
            info[i].append(j+1)

plan = list(map(int, input().split()))
visited = [False for _ in range(N+1)]

q = deque([plan[0]])
while (q):
    city = q.popleft()
    visited[city] = True
    for c in info[city]:
        if not visited[c]:
            q.append(c)

ans = "YES"
for city in plan:
    if not visited[city]:
        ans = "NO"
        break

print(ans)