import math

M = int(input())
N = int(input())
arr = []

for i in range(M, N+1):
    if i == 1: continue
    is_check = True
    for j in range(2, int(math.sqrt(i) + 1)):
        if i % j == 0:
            is_check = False
    if is_check: arr.append(i)
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])