arr = []
N = input()
while 1:
    if N[0:4] == "XXXX":
        arr.append("AAAA")
        N = N[4:]
    elif N[0:2] == "XX":
        arr.append("BB")
        N = N[2:]
    elif len(N) == 0:
        print(*arr, sep = "")
        break
    elif N[0] == ".":
        arr.append(".")
        N = N[1:]
    else:
        print(-1)
        break
