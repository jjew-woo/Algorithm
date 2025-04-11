def solution(k, tangerine):
    answer = 0
    count = {}
    for t in tangerine:
        if t in count:
            count[t] += 1
        else:
            count[t] = 1
    
    count = sorted(list(count.items()), key = lambda x:x[1], reverse=True)
    
    for c in count:
        if k <= 0:
            break
        k -= min(c[1], k)
        answer += 1
        
    return answer