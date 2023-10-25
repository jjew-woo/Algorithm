square = []
N, M = map(int, input().split())
for _ in range(N):
    square.append(list(map(int, input())))

for s in range(min(N,M), 1, -1):
    for i in range(N-s+1):
        for j in range(M-s+1):
            if square[i][j] == square[i+s-1][j] == square[i][j+s-1] == square[i+s-1][j+s-1]:
                print(s*s)
                exit()

print(1)