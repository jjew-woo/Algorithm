def solution(n, s, a, b, fares):
    charges = [ [int(1e9)]*(n+1) for _ in range(n+1) ]
    
    for i in range(1, n+1):
        charges[i][i] = 0
        
    for fare in fares:
        charges[fare[0]][fare[1]] = charges[fare[1]][fare[0]] = fare[2]
        
    for k in range(1, n+1):
        for x in range(1, n+1):
            for y in range(1, n+1):
                charges[x][y] = min(charges[x][y], charges[x][k]+charges[k][y])

    # s에서 a까지, s에서 b까지 둘 다 따로 가는 경우로 초기화
    charge = charges[s][a] + charges[s][b]
    
    # s에서 a까지, s에서 b까지 -> 1~n까지 거쳐서 가는 경로
    for i in range(1, n+1):
        charge = min(charge, charges[s][i] + charges[i][a] + charges[i][b])
    
    return charge