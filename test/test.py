import datetime
a = list(map(int, input().split()))
b = list(map(int, input().split()))
date1 = datetime.datetime(a[0],a[1],a[2])
date2 = datetime.datetime(b[0],b[1],b[2])
if (date2 - date1).days >= 365243:
    print('gg')
    exit()
print(f'D-{(date2-date1).days}')