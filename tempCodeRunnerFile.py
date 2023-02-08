a, b, c = map(int, input().split())
d = int(input())
# a, b, c, d = 14, 30, 0, 200

times = (a * 3600) + (b * 60) + c + d

if times//3600 >= 24:
    print(f"{(times//3600)-24} {(times%3600)//60} {((times%3600)%60)}")
else:
    print(f"{times//3600} {(times%3600)//60} {((times%3600)%60)}")