def solution(msg):
    answer = []
    dic = {chr(ord('A')+i):i+1 for i in range(26)}
    
    n = 27; s = 0; e = 1
    while True:
        if e == len(msg)+1:
            answer.append(dic[msg[s:e]])
            break
            
        if msg[s:e] in dic:
            e += 1
        else:
            answer.append(dic[msg[s:e-1]])
            dic[msg[s:e]] = n
            n += 1
            s = e-1

    return answer