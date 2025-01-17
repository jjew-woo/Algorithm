def solution(n, t, m, timetable):
    answer = [0, 0]
    timetable = sorted([ [int(t[:2]), int(t[3:])] for t in timetable])
    crew = 0
    
    for i in range(n):
        time = [9+((t*i)//60), (t*i)%60]
        for j in range(crew, len(timetable)):
            if (timetable[j][0] > time[0]) or (timetable[j][0] == time[0] and timetable[j][1] > time[1]) or (j == len(timetable)-1 and j-crew+1 < m):
                answer = time
                crew = j
                break
                
            if j - crew + 1 == m:
                answer = [timetable[j][0], timetable[j][1]-1] if timetable[j][1] != 0 else [timetable[j][0]-1, 59]
                crew = j+1
                break
                
    return str(answer[0]).zfill(2) + ':' + str(answer[1]).zfill(2)