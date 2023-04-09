dic = {
    '1' : 2,
    '2' : 3,
    '3' : 3,
    '4' : 3,
    '5' : 3,
    '6' : 3,
    '7' : 3,
    '8' : 3,
    '9' : 3,
    '0' : 4
}
while 1:
    N = input()
    if N == '0': break
    length = len(N)+1
    for i in range(len(N)):
        length += dic[N[i]]
    print(length)