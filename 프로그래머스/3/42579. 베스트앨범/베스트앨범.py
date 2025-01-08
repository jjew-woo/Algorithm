from collections import defaultdict

def solution(genres, plays):
    count = defaultdict(int)
    genre = defaultdict(list)
    
    for i in range(len(genres)):
        count[genres[i]] += plays[i]
        genre[genres[i]].append((plays[i], i))
        
    count = sorted(list(count.items()), key=lambda x: -x[1])
    
    answer = []
    for g in count:
        music = sorted(genre[g[0]], key=lambda x: (-x[0], x[1]))[:2]
        for m in music:
            answer.append(m[1])
    
    return answer