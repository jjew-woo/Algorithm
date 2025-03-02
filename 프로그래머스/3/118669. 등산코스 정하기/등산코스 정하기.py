import heapq

def solution(n, paths, gates, summits):
    answer = []
    INF = 10000001  
    graph = [ [] for _ in range(n+1) ]
    intens = [INF]*(n+1)
    gates = set(gates)
    summits = set(summits)
    
    for path in paths:
        if path[0] not in gates and path[1] not in summits:
            graph[path[1]].append((path[0],path[2]))
        if path[1] not in gates and path[0] not in summits:
            graph[path[0]].append((path[1],path[2]))
            
    q = []
    for gate in gates:
         heapq.heappush(q, (0,gate))

    while q:
        inten, node = heapq.heappop(q)
        if intens[node] < inten:
            continue
        for j in graph[node]:
            intensity = max(inten, j[1])
            if intensity < intens[j[0]]:
                intens[j[0]] = intensity
                heapq.heappush(q, (intensity, j[0]))
    
    for summit in summits:
        answer.append([summit,intens[summit]])
        
    return sorted(answer, key = lambda x : (x[1], x[0]))[0]