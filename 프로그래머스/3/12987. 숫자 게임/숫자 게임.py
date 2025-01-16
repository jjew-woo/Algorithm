def solution(A, B):
    answer = 0
    idx = 0
    
    A.sort(); B.sort()
    for i in range(len(B)):
        if A[idx] < B[i]:
            answer += 1
            idx += 1
    
    return answer