def update1(r,c,value,table):
    r,c = table[r][c] if isinstance(table[r][c], list) else [r,c]
    table[r][c] = value
    return table

def update2(v1, v2, table):
    for i in range(51):
        for j in range(51):
            if table[i][j] == v1:
                table[i][j] = v2
    return table

def merge(r1, c1, r2, c2, table, merge_info):
    r, c = table[r1][c1] if isinstance(table[r1][c1], list) else [r1,c1]
    i, j = table[r2][c2] if isinstance(table[r2][c2], list) else [r2,c2]
    if (r,c) == (i,j):
        return
    if table[r][c] == "EMPTY": table[r][c] = table[i][j]
    table[i][j] = [r,c]
    for y, x in merge_info[i][j]:
        table[y][x] = [r,c]
        merge_info[r][c].append([y,x])
    merge_info[r][c].append([i,j])
    merge_info[i][j] = []
    return table, merge_info

def unmerge(r, c, table, merge_info):
    i,j = table[r][c] if isinstance(table[r][c], list) else [r,c]
    value = table[i][j]
    table[i][j] = "EMPTY"
    for y,x in merge_info[i][j]:
        table[y][x] = "EMPTY"
    merge_info[i][j] = []
    table[r][c] = value
    return table

def print1(r, c, table):
    r,c = table[r][c] if isinstance(table[r][c], list) else [r,c]
    return table[r][c]

def solution(commands):
    answer = []
    table = [["EMPTY" for _ in range(51)] for _ in range(51)]
    merge_info = [[[] for _ in range(51)] for _ in range(51)]
    
    for command in commands:
        c = command.split(' ')
        if c[0] == "UPDATE":
            update1(int(c[1]), int(c[2]), c[3], table) if len(c) == 4 else update2(c[1], c[2], table)
        elif c[0] == "MERGE":
            merge(int(c[1]), int(c[2]), int(c[3]), int(c[4]), table, merge_info)
        elif c[0] == "UNMERGE":
            unmerge(int(c[1]), int(c[2]), table, merge_info)
        elif c[0] == "PRINT":
            answer.append(print1(int(c[1]), int(c[2]), table))

    return answer