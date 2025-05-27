def cal(time):
    return int(time[:2])*60+int(time[3:])

def solution(plans):
    answer = []
    plans.sort(key = lambda x : x[1])
    
    stop = []
    for i in range(len(plans)-1):
        name, start, playtime = plans[i][0], cal(plans[i][1]), int(plans[i][2])
        
        end = start + playtime
        next_start = cal(plans[i+1][1])
        if end > next_start:
            stop.append([name, playtime-(next_start-start)])
        else:
            answer.append(name)
            remaining = next_start - end
            while remaining > 0 and stop:
                name, playtime = stop.pop()
                remaining -= playtime
                if remaining >= 0:
                    answer.append(name)
                else:
                    stop.append([name, -(remaining)])

    return answer + [plans[-1][0]] + [hw[0] for hw in stop[::-1]]