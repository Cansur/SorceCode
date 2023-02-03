a, b = map(int, input().split())

def Binary_Search(start, end, target):
    mid = (start + end) / 2
    if(mid < target): start = mid + 1; Binary_Search(start, end, target)
    if(mid > target): end = mid - 1; Binary_Search(start, end, target)
    else:
        return mid

print(Binary_Search(1, 100, 50)