t = 0
N = int(input())
weight = sorted(list(map(int, input().split())))
M = int(input())
box = sorted(list(map(int, input().split())), reverse=True)

idx = 0
for i in range(N):
    if weight[i] < box[-1]:
        idx = i

is_move = [False for _ in range(M)]
if box[0] <= weight[-1]:
    while True:
        if not is_move.count(False):
            break
        
        is_possible = False
        for w in weight[idx:]:
            for i in range(M):
                if not is_move[i] and box[i] <= w:
                    is_possible = True
                    is_move[i] = True
                    break
        
        if not is_possible:
            t = 0
            break
        t += 1

print(t) if t else print(-1)