import re

def check(user_id, b_id):
    id_list = []
    l = len(b_id)
    b_id = re.compile(b_id.replace('*', '.'))
    for u_id in user_id:
        if len(u_id) == l and b_id.match(u_id):
            id_list.append(u_id)
    return id_list

def dfs(banned_id, ban_list, i, visited, l, id_list):
    if i == len(banned_id):
        l.sort()
        if l not in id_list:
            id_list.append(l)
        return id_list
    for ban_id in ban_list[banned_id[i]]:
        if not visited[ban_id]:
            visited[ban_id] = True
            dfs(banned_id, ban_list, i+1, visited, l+[ban_id], id_list)
            visited[ban_id] = False

def solution(user_id, banned_id):
    ban_list = {}
    visited = {i:False for i in user_id}
    id_list = []
    for b_id in banned_id:
        if b_id not in ban_list:
            ban_list[b_id] = check(user_id, b_id)
    dfs(banned_id, ban_list, 0, visited, [], id_list)
    
    return len(id_list)