n, m = map(int, input().split())
n_list = [i for i in range(1, n+1)]
for i in range(m):
    i, j = map(int, input().split())
    temp = n_list[j-1]
    n_list[j-1] = n_list[i-1]
    n_list[i-1] = temp
print(*n_list)
