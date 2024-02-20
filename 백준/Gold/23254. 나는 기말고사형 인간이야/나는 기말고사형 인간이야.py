from queue import PriorityQueue

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

score = PriorityQueue()
for i in range(M):
    score.put((-b[i], i))

total = 24*N
while total > 0 and not score.empty():
    s, i = score.get(); s = -(s)
    t = min(total, (100-a[i])//s)
    a[i] += (s*t); total -= t

    if a[i] < 100:
        score.put((-(100-a[i]), i))

print(sum(a))