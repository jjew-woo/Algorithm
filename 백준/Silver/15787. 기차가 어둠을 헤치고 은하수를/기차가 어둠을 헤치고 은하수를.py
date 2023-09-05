N, M = map(int, input().split())
train = [['0' for _ in range(20)] for _ in range(N)]

for _ in range(M):
    command = list(map(int, input().split()))
    if command[0] == 1:
        train[command[1]-1][command[2]-1] = '1'
    elif command[0] == 2:
        train[command[1]-1][command[2]-1] = '0'
    elif command[0] == 3:
        train[command[1]-1].insert(0,'0')
        train[command[1]-1].pop()
    elif command[0] == 4:
        train[command[1]-1].pop(0)
        train[command[1]-1].append('0')

print(len(set(''.join(t) for t in train)))