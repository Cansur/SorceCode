n, m = map(int, input().split())
# n, m = 5,4
n_list = [i for i in range(1, n+1)]
for i in range(m):
    temp = []
    d = 0
    i, j = map(int, input().split())
    # i, j = 1, 2
    for k in range(i-1, j):
        temp.append(n_list[k])
    temp.reverse()
    for k in range(i-1, j):
        n_list[k] = temp[d]
        d +=1
print(*n_list)

# 2 1 4 3 5
# 3 4 1 2 5