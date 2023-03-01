n = int(input())
arr_n = []
for _ in range(n):
    arr_n.append(int(input()))
arr_nn = [i for i in range(0, n+1)]
index = 0
arr_answer = []

while True:
    if arr_n[0] == arr_nn[index]:
        arr_nn.pop(index)
        arr_n.pop(0)
        index -= 1
        arr_answer.append('-')
    elif arr_n[0] > arr_nn[index]:
        index += 1
        arr_answer.append('+')
    elif arr_n[0] < arr_nn[index]:
        arr_answer = []
        break
    if len(arr_nn) == 1:
        break
if len(arr_answer) == 0:
    print('NO')
else:
    print(*arr_answer)