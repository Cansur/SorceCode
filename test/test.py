from sys import stdin
n = int(input())
xy = []
for _ in range(n):
    xy.append(list(map(int, stdin.readline().split())))
xy = sorted(xy)
for i in range(n):
    print(*xy[i])