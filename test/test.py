N = int(input())
x = list(map(int, input().split()))
a, b = 0, 0
for i in x:
    a += (i // 30) + 1
    b += (i // 60) + 1
a *= 10; b *= 15
if a < b: print('Y', a)
if a > b: print('M', b)
if a == b: print('Y M', b)
# 71초를 사용
# 영식은 30초 마다 계산 : 61 + 10 = 30 + 10