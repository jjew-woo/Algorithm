def is_changeable(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    answer = 0
    visited = [False for _ in range(len(words))]
    
    def bfs(word, level):
        nonlocal answer
        
        if word == target:
            answer = level
            return
        if level == len(words)-1:
            return
        
        for i in range(len(words)):
            if not visited[i] and is_changeable(word, words[i]):
                visited[i] = True
                bfs(words[i], level+1)
                visited[i] = False
    
    bfs(begin, 0)
    return answer