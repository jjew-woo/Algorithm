def dfs(graph, com, visited):
    visited[com] = True
    for i in graph[com]:
        if not visited[i]:
            dfs(graph, i, visited)
    
def solution(n, computers):
    count = 0
    graph = [[j for j in range(n) if computers[i][j] and j != i] for i in range(n)]
    visited = [False] * n
    
    for c in range(n):
        if not visited[c]:
            count += 1
            dfs(graph, c, visited)
    
    return count