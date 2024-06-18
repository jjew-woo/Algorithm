import heapq

N, M = map(int, input().split())
time = []; charging = []

for num in list(map(int, input().split())):
    heapq.heappush(time, (-num, num))

t = 0
while time:
    if len(charging) >= M:
        t = heapq.heappop(charging)
    heapq.heappush(charging, t + heapq.heappop(time)[1])

print(max(charging))