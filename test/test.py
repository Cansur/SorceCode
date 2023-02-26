import sys

n = int(sys.stdin.readline())
list = []
for i in range(n):
    typenum = sys.stdin.readline().split()
    
    if typenum[0] == 'push':
        list.append(typenum[1])
    elif typenum[0] == 'pop':
        if len(list) == 0:
            print(-1)
        else:
            print(list.pop(0))
    elif typenum[0] == 'size':
        print(len(list))
    elif typenum[0] == 'empty':
        if len(list) == 0:
            print(1)
        else:
            print(0)
    elif typenum[0] == 'front':
        if len(list) == 0:
            print(-1)
        else:
            print(list[0])
    elif typenum[0] == 'back':
        if len(list) == 0:
            print(-1)
        else:
            print(list[-1])
    