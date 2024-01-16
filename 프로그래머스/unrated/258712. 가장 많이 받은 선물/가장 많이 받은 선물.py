from itertools import combinations

def solution(friends, gifts):
    answer = { f : 0 for f in friends }
    give = { f1 : { f2 : 0 for f2 in friends if f1 != f2 } for f1 in friends }
    take = { f1 : { f2 : 0 for f2 in friends if f1 != f2 } for f1 in friends }
    
    for gift in gifts:
        a, b = gift.split(' ')
        give[a][b] += 1
        take[b][a] += 1
    index = { f : (sum(give[f].values())-sum(take[f].values())) for f in friends }

    for a,b in combinations(friends, 2):
        if give[a][b] > give[b][a]:
            answer[a] += 1
        elif give[a][b] < give[b][a]:
            answer[b] += 1
        else:
            if index[a] > index[b]:
                answer[a] += 1
            elif index[a] < index[b]:
                answer[b] += 1

    return max(answer.values())