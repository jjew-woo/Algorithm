def solution(topping):
    answer = 0
    A = set(); A_cnt = 0
    B = {}; B_cnt = len(set(topping))
    for num in topping:
        if num in B:
            B[num] += 1
        else:
            B[num] = 1

    for num in topping:
        if num not in A:
            A_cnt += 1
            A.add(num)
        B[num] -= 1
        if B[num] == 0:
            B_cnt -= 1
        
        if A_cnt == B_cnt:
            answer += 1

    return answer