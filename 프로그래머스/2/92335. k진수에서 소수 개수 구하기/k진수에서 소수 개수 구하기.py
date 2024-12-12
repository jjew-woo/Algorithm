import math

def is_prime(n):
    if n < 2:
        return False
    
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True

def convert(n, k):
    s = ''
    while n:
        s += str(n%k)
        n //= k
    return s[::-1]
    
def solution(n, k):
    cnt = 0
    P = convert(n,k).split('0')
    
    for x in P:
        if x != '' and is_prime(int(x)):
            cnt += 1
    return cnt