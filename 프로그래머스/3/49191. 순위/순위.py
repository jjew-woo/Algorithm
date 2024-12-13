from collections import deque

def solution(n, results):
    answer = 0
    win = [[0 for _ in range(n+1)] for _ in range(n+1)]
    lose = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for w, l in results:
        win[w][l] = 1
        lose[l][w] = 1
    
    for i in range(1, n+1):
        visited = [0 for _ in range(n+1)]
        q = deque([i])
        
        while q:
            p = q.popleft()
            visited[p] = 1
            for j in range(1,n+1):
                if win[p][j] and not(visited[j]):
                    q.append(j)
                    visited[j] = 1
        visited[i] = 0
        win[i] = visited
    
    for i in range(1, n+1):
        visited = [0 for _ in range(n+1)]
        q = deque([i])
        
        while q:
            p = q.popleft()
            visited[p] = 1
            for j in range(1,n+1):
                if lose[p][j] and not(visited[j]):
                    q.append(j)
                    visited[j] = 1
        visited[i] = 0
        lose[i] = visited
    
    for i in range(1, n+1):
        if win[i].count(1) + lose[i].count(1) == n-1:
            answer += 1
            
    return answer