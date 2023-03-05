N = int(input())
cnt = N//5

while True:
    if (N-(cnt*5))%3 == 0:
        cnt += (N-(cnt*5))/3
        if cnt != int(cnt):
            print(-1)
            break
        print(int(cnt))
        break
    elif cnt <= 0:
        print(-1)
        break
    else:
        cnt -= 1



