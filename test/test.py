for _ in range(int(input())):
    k = int(input())
    n = int(input())
    arr_inc = [i for i in range(1, n+1)]
    arr_get = [0 for _ in range(n)]
    for i in range(k-1):
        for j in range(n):
            for p in range(j+1):
                arr_get[j] += arr_inc[p]
        arr_inc = arr_get
        arr_get = [0 for _ in range(n)]
    print(sum(arr_inc))

# 3층 1 5 15 35
# 2층 1 4 10 20
# 1층 1 3 6 10
# 0층 1 2 3 4