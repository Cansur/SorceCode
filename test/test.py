idx = 0
for _ in range(int(input())):
    is_check = True
    str = input()
    for i in range(len(str)-1):
        if str[i] != str[i+1]:
            check_str = str[i+1:]
            if check_str.count(str[i]) > 0:
                is_check = False
    if is_check:
        idx += 1
print(idx)