N, S = map(int, input().split())
sequence = list(map(int, input().split()))
ans = 0

def check(num):
    return 1 if num == S else 0

def dfs(sum, i):
    global ans
    if i == N:
        ans += check(sum)
        return
    
    dfs(sum+sequence[i], i+1)
    dfs(sum, i+1)

for i in range(N):
    dfs(sequence[i], i+1)

print(ans)