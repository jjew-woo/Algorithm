def solution(rows, columns, queries):
    answer = []
    matrix = []
    for n in range(1, columns*(rows-1)+2, columns):
        matrix.append([i for i in range(n, n+columns)])   
    
    for q in queries:
        num = [matrix[q[0]-1][q[1]-1]]
        
        for i in range(q[1], q[3]):
            num.append(matrix[q[0]-1][i])
            matrix[q[0]-1][i] = num[-2]
            
        for i in range(q[0], q[2]):
            num.append(matrix[i][q[3]-1])
            matrix[i][q[3]-1] = num[-2]
            
        for i in range(q[3]-2, q[1]-2, -1):
            num.append(matrix[q[2]-1][i])
            matrix[q[2]-1][i] = num[-2]
            
        for i in range(q[2]-2, q[0]-2, -1):
            num.append(matrix[i][q[1]-1])
            matrix[i][q[1]-1] = num[-2]
            
        answer.append(min(num))  
        
    return answer