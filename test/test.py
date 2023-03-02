N, M = map(int, input().split())
arr_tree = list(map(int, input().split()))
start, end = 1, max(arr_tree)

while start <= end:
    mid = (start+end) // 2
    
    length = 0 
    for i in arr_tree:
        if i >= mid:
            length += i - mid
    
    if length >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)