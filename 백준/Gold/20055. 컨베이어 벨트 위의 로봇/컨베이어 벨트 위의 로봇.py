ans = 0
N, K = map(int, input().split())
dur = list(map(int, input().split()))
l = 2*N; robot = [False for _ in range(l)]

move = -1
while True:
    ans += 1
    move = (move+1)%l                       # 벨트 회전
    start = l-(move+1)
    end = (start+N-1)%l
    for i in range(N-1,-1,-1):              # 로봇 이동
        idx = (start+i)%l
        if idx == end:                      # 내리는 위치에 로봇이 있으면 내림
            if robot[idx]:
                robot[idx] = False
        else:
            if robot[idx]:                  # 로봇이 이동할 수 있으면 이동하고 내구도 -1
                next = (idx+1)%l
                if (dur[next]) and (not robot[next]):
                    robot[idx] = False
                    dur[next] -= 1
                    if next != end:         # 내리는 위치면 즉시 내림
                        robot[next] = True
    if dur[start]:                          # 올리는 위치에 내구도가 0이 아니면 올림
        dur[start] -= 1
        robot[start] = True

    if dur.count(0) >= K:                   # 내구도가 0인 칸의 개수가 K개 이상이면 종료
        break

print(ans)