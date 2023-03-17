import sys
from collections import Counter
N = int(input())
arr = [int(sys.stdin.readline()) for _ in range(N)]
arr.sort()

def mode():
    cnt = Counter(arr).most_common(2)
    if len(arr) > 1:
        if cnt[0][1] == cnt[1][1]:
            return cnt[1][0]
        else:
            return cnt[0][0]
    else:
        return cnt[0][0]

print(round(sum(arr)/N))
print(arr[N//2])
print(mode())
print(arr[-1] - arr[0])