import sys
sys.setrecursionlimit(3000)

def dfs(y,x):
    if x <= -1 or x >= m or y <= -1 or y >= n:
        return False
    if x in graph[y]:
        del graph[y][graph[y].index(x)]
        
        dfs(y-1, x)
        dfs(y, x-1)
        dfs(y+1, x)
        dfs(y, x+1)
        return True
    return False

T = int(input())

for _ in range(T):
    m, n, k = map(int, input().split())
    graph = [[] for _ in range(n)]
    result = 0

    for _ in range(k):
        num, i = map(int, input().split())
        graph[i].append(num)

    for i in range(n):
        for j in range(m):
            if dfs(i, j) == True:
                result += 1

    print(result)