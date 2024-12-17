def solution(m, n, puddles):
    board = [[0]*(m+1) for _ in range(n+1)]
    board[1][1] = 1
    
    for i in range(1,n+1):
        for j in range(1,m+1):
            if [j,i] not in puddles and [i,j] != [1,1]:
                board[i][j] = board[i-1][j] + board[i][j-1]

    return board[n][m]%1000000007