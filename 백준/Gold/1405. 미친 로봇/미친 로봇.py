def dfs(y, x, cnt, per):
    if cnt == n:
        global ans
        ans += per
        return
    
    board[y][x] = True
    for i in range(4):
        ny = y+d[i][0]; nx = x+d[i][1]

        if not board[ny][nx]:
            dfs(ny, nx, cnt+1, per*dp[i])
            board[ny][nx] = False

ans = 0
n, pe, pw, ps, pn = map(int, input().split())
dp = [pe/100, pw/100, ps/100, pn/100]
board = [[False for _ in range(30)] for _ in range(30)]
d = [[0,1], [0, -1], [1, 0], [-1, 0]]
dfs(15, 15, 0, 1.0)
print(ans)