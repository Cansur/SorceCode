data = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0
}
sum = 0; a_sum = 0
for _ in range(20):
    k, a, b = input().split()
    a = float(a)
    if b == 'P': continue
    sum += a*data[b]
    a_sum += a
print('{:.6f}'.format(sum/a_sum))