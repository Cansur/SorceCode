while True:
    n, m, o = map(int, input().split())
    if n+m+o == 0: break
    big = max(n,m,o)
    if big == n: 
        n = o
    if big == m: 
        m = o 
    if big**2 == n**2 + m**2:
        print('right')
    else:
        print('wrong')