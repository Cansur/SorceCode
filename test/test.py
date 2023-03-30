N, B = input().split()
arr = []; sum = 0
for i in N:
    arr.append(i)
for i in range(len(arr)):
    if(ord(arr[i]) >= 65):
        sum += (ord(arr[i])-55)*(int(B)**(len(arr)-i-1))
    else:
        sum += int(arr[i])*(int(B)**(len(arr)-i-1))
print(sum)