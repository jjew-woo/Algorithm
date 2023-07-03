from collections import deque 

def bfs(cheese, i, j, n ,m):
    melt = []
    visited = [[False for _ in range(m)] for _ in range(n)]
    q = deque([(i,j)])
    visited[i][j] = True
    while q:
        y, x = q.popleft()
        for dy, dx in ((-1,0), (1, 0), (0, 1), (0, -1)):
            ny = y + dy; nx = x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            
            if not visited[ny][nx]:
                if cheese[ny][nx]:
                    melt.append((ny, nx))
                else:
                    q.append((ny,nx))
                visited[ny][nx] = True
    
    for y,x in melt:
        cheese[y][x] = 0

    return cheese            


n,m = map(int, input().split())
cheese = []
t = 0
cnt = 0

for _ in range(n):
    cheese.append(list(map(int, input().split())))

while (sum(cheese, []).count(1) != 0):
    cnt = sum(cheese, []).count(1)
    cheese = bfs(cheese, 0, 0, n, m)
    t += 1

print(t)
print(cnt)