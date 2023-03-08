import sys
N = int(input())
X = list(map(int, sys.stdin.readline().split()))
ranks = sorted(list(set(X)))
dict = {ranks[i] : i for i in range(len(ranks))}
for i in X:
    print(dict[i], end = ' ')