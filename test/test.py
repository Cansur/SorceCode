for _ in range(int(input())):
    C = int(input())
    quarter = C//25
    dime = (C-quarter*25)//10
    nickel = (C-quarter*25-dime*10)//5
    penny = (C-quarter*25-dime*10-nickel*5)
    print(quarter, dime, nickel, penny)