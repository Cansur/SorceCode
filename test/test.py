for _ in range(int(input())):    
    h, w, n = map(int, input().split())
    floor = n%h
    room = (n//h)+1
    if floor == 0: floor = h; room -= 1
    if room < 10:
        print(str(floor) + '0' + str(room))
    else:
        print(str(floor) + str(room))