from collections import deque

N, M = map(int, input().split())
maze = []
visited = [[0 for _ in range(N)] for _ in range(M)]; visited[0][0] = 1

for _ in range(M):
    maze.append(list(map(int, list(input()))))

q = deque([(0,0)])

while q:
    y, x = q.popleft()

    for dy, dx in [(1,0), (0,1), (-1, 0), (0,-1)]:
        ny = y+dy; nx = x+dx

        if ny < 0 or ny >= M or nx < 0 or nx >= N:
            continue
        
        if visited[ny][nx]:
            if visited[y][x] + maze[ny][nx] < visited[ny][nx]:
                visited[ny][nx] = visited[y][x] + maze[ny][nx]
                q.append((ny, nx))
        else:
            visited[ny][nx] = visited[y][x] + maze[ny][nx]
            q.append((ny, nx))

print(visited[M-1][N-1]-1)