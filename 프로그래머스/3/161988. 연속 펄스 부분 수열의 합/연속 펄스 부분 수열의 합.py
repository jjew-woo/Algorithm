'''
1   => [2,-3,-6,-1,3,1,2,-4] => [2,-1,-6,-1,3,4,6,2]
-1  => [-2,3,6,1,-3,-1,-2,4] => [-2,3,9,10,7,6,4,8]
'''
def solution(sequence):
    plus = [sequence[0]]; minus = [-(sequence[0])]
    
    for i in range(1,len(sequence)):
        num = -(sequence[i])
        if i%2:
            plus.append(max(plus[-1]+num,num))
            minus.append(max(minus[-1]+sequence[i],sequence[i]))
        else:
            minus.append(max(minus[-1]+num,num))
            plus.append(max(plus[-1]+sequence[i],sequence[i]))

    return max(plus+minus)