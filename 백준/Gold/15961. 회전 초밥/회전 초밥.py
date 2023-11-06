from collections import defaultdict

N, d, k, c = map(int, input().split())
belt = []

for _ in range(N):
    belt.append(int(input()))

count = defaultdict(int)
for i in range(k):
    count[belt[i]] += 1

max_type = len(count) if c in count else len(count)+1
type_cnt = max_type
for i in range(N):
    s, e = belt[i], belt[(i+k)%N]
    count[s] -= 1
    if count[s] == 0:
        if s != c:
            type_cnt -= 1

    count[e] += 1
    if count[e] == 1:
        if e != c:
            type_cnt += 1

    max_type = max(max_type, type_cnt)

print(max_type)