import sys
while 1:
    N = int(sys.stdin.readline())
    arr = []
    if N == -1: break

    for i in range(1, N):
        if N % i == 0: arr.append(i)
    
    if sum(arr) == N:
        print(f'{N} = 1', end = '')
        for i in range(1, len(arr)):
            print(f' + {arr[i]}', end = '')
        print()
    else:
        print(f'{N} is NOT perfect.')