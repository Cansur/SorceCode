cnt = 1
while 1:
    N = int(input())
    if(N == 0): break
    arr = [];  cntA = 0
    for _ in range(N):
        arr.append(list(input().split()))
    if(cnt > 1): print("")
    print("Group", cnt)
    cnt += 1
    for i in range(N):
        for j in range(1, len(arr[i])):
            if "N" in arr[i][j]:
                cntA += 1
                name = arr[i][0]
                number = i - j
                if(number < 0 ): number += N
                print(arr[number][0], "was nasty about", arr[i][0])
    if(cntA == 0): print("Nobody was nasty")

    
            