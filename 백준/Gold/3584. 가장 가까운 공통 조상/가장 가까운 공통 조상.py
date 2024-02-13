def search(tree, n1, n2):
    p1 = set(); p2 = set()

    while n1 or n2:
        if n1 == n2:
            return n1
        if n1 in p2:
            return n1
        if n2 in p1:
            return n2

        if n1: p1.add(n1)
        if n2: p2.add(n2)

        n1 = tree[n1]; n2 = tree[n2]

T = int(input())

for _ in range(T):
    N = int(input())
    tree = [0 for _ in range(N+1)]
    for _ in range(N-1):
        a,b = map(int, input().split(" "))
        tree[b] = a

    n1, n2 = map(int, input().split(" "))
    print(search(tree, n1, n2))