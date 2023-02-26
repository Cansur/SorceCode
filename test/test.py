n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

counts = {}
for i in n_list:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

for i in m_list:
    if counts.get(i) == None:
        print('0', end = ' ')
    else:
        print(counts[i], end = ' ')