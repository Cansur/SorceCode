K = int(input())
arr = []
for _ in range(K):
    var = int(input())
    if var == 0: arr.pop()
    else: arr.append(var)
print(sum(arr))