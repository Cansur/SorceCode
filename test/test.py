
n, k = map(int, input().split())
arr_n = [i for i in range(1, n+1)]
arr_answer = []
index_n = 0
for i in range(n):
    index_n += k-1
    if index_n >= len(arr_n):
        index_n %= len(arr_n)
    arr_answer.append(arr_n.pop(index_n))
print('<', end = '')
print(*arr_answer, sep= ', ', end = '')
print('>', end = '')