from collections import defaultdict

def solution(edges):
    answer = [0,0,0,0]
    in_d = defaultdict(int)
    out_d = defaultdict(int)
    
    n = 0
    for a,b in edges:
        in_d[b] += 1
        out_d[a] += 1
        n = max(a,b,n)
    
    for i in range(1, n+1):
        if out_d[i] >= 2 and in_d[i] == 0:
            answer[0] = i
        elif out_d[i] == 0:
            answer[2] += 1
        elif out_d[i] >= 2 and in_d[i] >= 2:
            answer[3] += 1
    answer[1] = out_d[answer[0]] - answer[2] - answer[3]

    return answer