dic = {}; cnt = 0
for _ in range(int(input())):
    str = input()
    if str == 'ENTER':
        dic = {}
        continue
    if dic.get(str):
        continue
    else:
        dic[str] = 1
        cnt += 1
print(cnt)