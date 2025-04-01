import heapq
import sys
small, big = [], []

N = int(sys.stdin.readline())
mid = int(sys.stdin.readline())
print(mid)
for _ in range(N-1):
    n = int(sys.stdin.readline())
    if n > mid:
        heapq.heappush(big, n)
        if len(big) - len(small) > 1:
            heapq.heappush(small, -mid)
            mid = heapq.heappop(big)
    else:
        heapq.heappush(small, -n)
        if len(small) > len(big):
            heapq.heappush(big, mid)
            mid = -(heapq.heappop(small))
    print(mid)