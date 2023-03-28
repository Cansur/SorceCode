arr = [[0] * 15 for _ in range(5)]
for idx in range(5):
    str = input()
    for i in range(len(str)):
        arr[idx][i] = str[i]
str = ''
for i in range(15):
    for j in range(5):
        if arr[j][i] == 0: continue
        str += arr[j][i]
print(str)
     
# arr = ['WS']

# try:
#     print(arr[0][2])
# except IndexError:
#     print('')