table = []
n, m = map(int, input().split())

for _ in range(n):
    table.append(list(map(int, input())))

k = int(input())

ans = [0]*n
for i in range(n):
    cnt = table[i].count(0)
    if k%2:
        if cnt%2 and cnt <= k:
            for j in range(n):
                if table[i] == table[j]:
                    ans[i] += 1
    else:
        if not cnt%2 and cnt <= k:
            for j in range(n):
                if table[i] == table[j]:
                    ans[i] += 1

print(max(ans))