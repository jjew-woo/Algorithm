import sys

N, M = map(int, sys.stdin.readline().rstrip().split(" "))
book = {}

for i in range(1, N+1):
    poketmon = sys.stdin.readline().rstrip()
    book[str(i)] = poketmon
    book[poketmon] = str(i)

for _ in range(M):
    print(book[sys.stdin.readline().rstrip()])