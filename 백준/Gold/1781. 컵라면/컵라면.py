import heapq

N = int(input())
problem = [list(map(int, input().split())) for _ in range(N)]
problem.sort()

q = []
for d, c in problem:
    heapq.heappush(q, c)
    if d < len(q):
        heapq.heappop(q)

print(sum(q))