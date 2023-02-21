n, m = map(int, input().split())
n_list = [0 for _ in range(n)]
for p in range(m):
    i, j, k = map(int, input().split())
    for q in range(i-1, j):
        n_list[q] = k
print(*n_list)
