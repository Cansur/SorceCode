import sys
N = int(sys.stdin.readline())
dic = {}
dic = dict.fromkeys(map(int, sys.stdin.readline().split()), 1)
M = int(sys.stdin.readline())
arr_M = list(map(int, sys.stdin.readline().split()))

for i in range(M):
    if dic.get(arr_M[i]):
        print(1, end = ' ')
    else:
        print(0, end = ' ')