from itertools import permutations 

def solution(k, dungeons):
    answer = -1
    for order in list(permutations([i for i in range(len(dungeons))], len(dungeons))):
        f = k; count = 0
        for o in order:
            if dungeons[o][0] > f:
                break
            count += 1
            f -= dungeons[o][1]
        
        if count == len(dungeons):
            return count
        
        answer = max(answer, count)
    return answer