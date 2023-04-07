s = input()
li = []
for i in range(len(s)-2):
    for j in range(i+1, len(s)-1):
        for k in range(j+1, len(s)):
            s1 = s[:j][::-1]
            s2 = s[j:k][::-1] 
            s3 = s[k:][::-1]
            t = s1 + s2 + s3
            li.append(t)
print(min(li))