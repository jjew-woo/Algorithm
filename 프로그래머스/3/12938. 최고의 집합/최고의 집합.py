def solution(n, s):
    if n > s:
        return [-1]
    
    answer = []
    res = s//n
    t = s%n
    for i in range(0, n):
        if i >= n - t:
            answer.append(res + 1)
        else:
            answer.append(res)
            
    return answer