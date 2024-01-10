from collections import deque

def count(n, graph, v1, v2):
    cnt = 0
    visited = [False for _ in range(n+1)]
    q = deque([v1])
    
    while q:
        v = q.popleft()
        visited[v] = True
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                if i != v2:
                    visited[i] = True
                    q.append(i)
    return abs(cnt - (n-cnt))

def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]
    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    for v1, v2 in wires:
        answer = min(answer, count(n, graph, v1, v2))

    return answer