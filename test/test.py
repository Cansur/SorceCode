n = input()
is_n = True
for i in range(len(n)//2):
    if n[i] != n[len(n)-i-1]:
        is_n = False
if is_n:
    print(1)
else:
    print(0)