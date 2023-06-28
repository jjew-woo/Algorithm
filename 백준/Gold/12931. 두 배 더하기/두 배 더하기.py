n = int(input())
b = list(map(int, input().split()))

cnt = 0
while True:
    if b.count(0) == n:
        break
    
    is_double = False
    for i in range(n):
        if b[i]:
            if b[i]%2:
                b[i] -= 1
                cnt += 1
            
            if b[i] and b[i]%2 == 0:
                b[i] //= 2
                is_double = True
    
    if is_double:
        cnt += 1

print(cnt)