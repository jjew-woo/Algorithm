from itertools import combinations

def solution(relation):
    keys = []
    for i in range(1, len(relation[0])+1):
        comb = list(map(set, list(combinations([i for i in range(len(relation[0]))],i))))
        for com in comb:
            r = []
            for n in range(len(relation)):
                s = ''
                for c in com:
                    s += relation[n][c]
                r.append(s)
                
            if len(set(r)) == len(relation):
                keys.append(com)
                for key in keys[:-1]:
                    if key.issubset(com):
                        keys.remove(com) 
                        break
        
    return len(keys)