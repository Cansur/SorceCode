n = int(input())
count = 1
var = n
while True:
    x = (var//10) + (var%10)
    new = ((var%10)*10) + (x%10)
    if n == new:
        print(count)
        break
    else:
        count += 1
        var = new