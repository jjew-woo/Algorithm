import heapq

def solution(n, works):
    heap = []
    for work in works:
        heapq.heappush(heap, (-work, work))
    
    for _ in range(n):
        work = heapq.heappop(heap)[1] - 1
        if work < 0:
            break
        heapq.heappush(heap, (-work, work))
    
    return sum([i[1]**2 for i in heap])