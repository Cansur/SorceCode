import sys
def isPrime(n):
    if n == 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())
    x, y = n//2, n//2
    while x > 0:
        if isPrime(x) and isPrime(y):
            print(x, y)
            break
        else:
            x -= 1
            y += 1