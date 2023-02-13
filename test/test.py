# combinations --> 모든합 구하는 함수
from itertools import combinations
# var_list = [20,7,23,19,10,15,25,8,13]
var_list = [int(input()) for _ in range(9)]
for i in combinations(var_list, 7):
    if sum(i) == 100:
        var_list = i
        break
var_list = list(var_list)
var_list.sort()
print(*var_list, sep = '\n')