import sys
input = sys.stdin.readline

N = int(input())
music = list(map(int, input().split(" ")))
cnt = [0 for _ in range(N)]
for i in range(1, N):
    cnt[i] = cnt[i-1]+1 if music[i-1] > music[i] else cnt[i-1]
for _ in range(int(input())):
    x, y = map(int, input().split(" "))
    print(cnt[y-1]-cnt[x-1])