board = [list(map(int, list(input()))) for _ in range(8)]
visited = [[False for _ in range(7)] for _ in range(8)]
used = [[False for _ in range(7)] for _ in range(7)]

def check(x, y):
    global used, visited
    if (x, y) == (7,7):
        return 1

    cnt = 0
    if y == 7:
        x += 1; y = 0

    if visited[x][y]:
        return check(x, y+1)

    visited[x][y] = True
    for dx, dy in [(0,1), (1,0)]:
        nx = x + dx; ny = y + dy
        if nx >= 8 or ny >= 7:
            continue
        
        n1, n2 = board[x][y], board[nx][ny]
        if not used[n1][n2] and not visited[nx][ny]:
            used[n1][n2] = used[n2][n1] = True
            visited[nx][ny] = True
            cnt += check(x, y+1)
            used[n1][n2] = used[n2][n1] = False
            visited[nx][ny] = False
    visited[x][y] = False
    return cnt

print(check(0, 0))