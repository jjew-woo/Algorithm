def solution(skill, skill_trees):
    answer = len(skill_trees)
    for tree in skill_trees:
        s = 0
        for t in tree:
            if t in skill:
                if s < skill.index(t):
                    answer -= 1
                    break
                elif s == skill.index(t):
                    s += 1
    return answer