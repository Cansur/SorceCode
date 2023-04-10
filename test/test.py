M = int(input())
answer = 1
for _ in range(M):
    x, y = map(int, input().split())
    if answer == x:
        answer = y
    elif answer == y:
        answer = x
print(answer)