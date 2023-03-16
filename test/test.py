K, N = map(int, input().split())
arr = [int(input()) for _ in range(K)]

start, end = 1, max(arr)

while start <= end:
    mid, ea = (start + end) // 2, 0
    for i in arr:
        ea += i // mid

    if ea >= N: start = mid + 1
    else: end = mid - 1

print(start-1)
        