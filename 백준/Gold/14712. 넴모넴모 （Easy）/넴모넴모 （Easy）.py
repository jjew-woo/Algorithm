N,M = map(int, input().split())
board = [[0 for _ in range(M+1)] for _ in range(N+1)]
ans = 0

def dfs(y, x):
    global ans
    if (y == N and x == M+1):
        ans += 1
        return
    
    if x == M+1:
        x = 1; y += 1
    
    if not (board[y-1][x] and board[y][x-1] and board[y-1][x-1]):
        board[y][x] = 1
        dfs(y, x+1)
        board[y][x] = 0
    dfs(y, x+1)

dfs(1,1)
print(ans)