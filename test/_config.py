from sys import stdin
from collections import deque
n = int(input())
dq = deque()
for i in range(n):
    input = stdin.readline().split()
    if input[0] == 'push_front':
        dq.appendleft(input[1])
    elif input[0] == 'push_back':
        dq.append(input[1])
    elif input[0] == 'pop_front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.popleft())
    elif input[0] == 'pop_back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq.pop())
    elif input[0] == 'size':
        print(len(dq))
    elif input[0] == 'empty':
        if len(dq) == 0:
            print(1)
        else:
            print(0)
    elif input[0] == 'front':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[0])
    elif input[0] == 'back':
        if len(dq) == 0:
            print(-1)
        else:
            print(dq[-1])