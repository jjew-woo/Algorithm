def check(amount, N, M, K):
    s = sum(amount[:M])
    ans = 1 if s < K else 0
    for i in range(N-1):
        s += (amount[(i+M)%N]-amount[i])
        if s < K: ans += 1
    return ans

T = int(input())

for _ in range(T):
    N,M,K = map(int, input().split())
    amount = list(map(int, input().split()))

    if N != M:
        print(check(amount, N, M, K))
    else:
        print(1) if sum(amount) < K else print(0)