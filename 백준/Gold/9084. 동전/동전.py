T = int(input())

for _ in range(T):
    n = int(input())
    coin = list(map(int, input().split()))
    m = int(input())
    price = [0 for _ in range(m+1)]
    price[0] = 1

    for c in coin:
        for i in range(c, m+1):
            price[i] += price[i-c]

    print(price[-1])