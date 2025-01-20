from collections import defaultdict

def find(a1, b1, c1, a2, b2, c2):
    if (a1*b2-a2*b1) == 0:
        return (0.1,0.1)
    return ((b1*c2-b2*c1)/(a1*b2-a2*b1), (c1*a2-a1*c2)/(a1*b2-a2*b1))

def solution(line):
    answer = []
    coord = defaultdict(list)
    for i in range(len(line)):
        a1, b1, c1 = line[i][0], line[i][1], line[i][2]
        for j in range(i+1,len(line)):
            a2, b2, c2 = line[j][0], line[j][1], line[j][2]
            px, py = find(a1,b1,c1,a2,b2,c2)
            if not px%1 and not py%1:
                coord[int(py)].append(int(px))

    l = max(list(sum(coord.values(),[])))-min(list(sum(coord.values(),[])))+1
    min_x = -(min(list(sum(coord.values(),[]))))
    for y in range(max(list(coord.keys())), min(list(coord.keys()))-1, -1):
        r = ['.']*l
        for x in coord[y]:
            r[x+min_x] = '*'
        answer.append(''.join(r))
    return answer