from collections import defaultdict

def solution(clothes):
    cloth = defaultdict(int)
    for c_name,c_type in clothes:
        cloth[c_type] += 1
    
    answer = 1
    for cnt in list(cloth.values()):
        answer *= (cnt+1)
    
    return answer-1