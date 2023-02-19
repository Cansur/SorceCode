a,b,c = map(int, input().split())

if b < c:
    var = a//(c-b)
    print(var + 1)
else:
    print(-1)