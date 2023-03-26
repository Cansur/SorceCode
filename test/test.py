import sys

N, M, B = map(int, sys.stdin.readline().split())
ground = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
answer = sys.maxsize
idx = 0

for target in range(257):
    max_target, min_target = 0, 0

    for i in range(N):
        for j in range(M):
            if ground[i][j] >= target:
                max_target += ground[i][j] - target
            else:
                min_target += target - ground[i][j]

    if max_target + B >= min_target:
        if min_target + (max_target * 2) <= answer:
            answer = min_target + (max_target * 2)
            idx = target
print(answer, idx)