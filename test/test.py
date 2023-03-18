arr_x, arr_y = [], []
for _ in range(3):
    x, y = map(int, input().split())
    arr_x.append(x)
    arr_y.append(y)

for i in range(3):
    if arr_x.count(arr_x[i]) == 1: x4 = arr_x[i]
    if arr_y.count(arr_y[i]) == 1: y4 = arr_y[i]
print(x4, y4)