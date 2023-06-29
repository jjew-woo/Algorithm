n,m = map(int, input().split())
friend = [[n+1]*(n) for _ in range(n)]
step = [[n+1]*(n) for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    friend[a][b] = 1; friend[b][a] = 1
    step[a][b] = 1; step[b][a] = 1


for i in range(n):
    step[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            if (step[i][k] + step[k][j] < step[i][j]):
                step[i][j] = step[i][k] + step[k][j]


step = [sum(s) for s in step ]
print(step.index(min(step))+1)