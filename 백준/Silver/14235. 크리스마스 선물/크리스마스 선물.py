import heapq

present = []
for _ in range(int(input())):
    a = list(map(int, input().split()))
    if a[0]:
        for p in a[1:]:
            heapq.heappush(present, -p)
    else:
        print(-heapq.heappop(present)) if len(present) else print(-1)