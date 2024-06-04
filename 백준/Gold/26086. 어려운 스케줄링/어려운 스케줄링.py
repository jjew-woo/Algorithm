from collections import deque
import sys

input = lambda: sys.stdin.readline().strip('\n')

N, Q, k = map(int, input().split())
cmd = [tuple(map(int, input().split())) for _ in range(Q)]

idx = max([i if q == 1 else 0 for i, (q, *p) in enumerate(cmd)])
is_reverse = sum([q == 2 for q, *p in cmd[:idx]]) % 2 == 1
schedule = sorted([p[0] for q, *p in cmd[:idx] if q == 0], reverse=is_reverse)
schedule = [schedule, schedule[::-1]]

add = [[], []]
for q, *p in cmd[idx:]:
    if q == 0:
        add[is_reverse].append(p[0])
    elif q == 2:
        is_reverse = not is_reverse

print((add[is_reverse][::-1]+schedule[is_reverse]+add[not is_reverse])[k-1])