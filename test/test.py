while 1:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    ans = 1
    for i in range(arr[0]):
        splitting_factor = arr[2*i + 1]
        pruned_branches = arr[2*i + 2]
        ans = ans*splitting_factor - pruned_branches
    print(ans)