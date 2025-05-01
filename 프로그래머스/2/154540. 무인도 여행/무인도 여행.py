def dfs(maps, m, n, i, j, visited):
    s = 0
    stack = [(i,j)]
    visited[i][j] = True
    
    while stack:
        y, x = stack.pop()
        s += int(maps[y][x])        
        for d in -2,0,2,4:
            ny = y + d//3; nx = x + d%3 - 1
            if ny < 0 or ny >= m or nx < 0 or nx >= n:
                continue
            if not visited[ny][nx]:
                if maps[ny][nx] != 'X':
                    visited[ny][nx] = True
                    stack.append((ny,nx))
        
    return s, visited
    
def solution(maps):
    answer = []
    m, n = len(maps), len(maps[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            if (not visited[i][j]) and maps[i][j] != 'X':
                s, visited = dfs(maps, m, n, i, j, visited)
                answer.append(s)
    return sorted(answer) if answer else [-1]