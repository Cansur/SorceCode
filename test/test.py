e_list = {
    'ABC' : 3,
    'DEF' : 4,
    'GHI' : 5,
    'JKL' : 6,
    'MNO' : 7,
    'PQRS' : 8,
    'TUV' : 9,
    'WXYZ' : 10
}
n = input()
var = 0
for k in n:     # n을 하나하나 쪼갠 문자 k 
    for i in e_list:    # e_list안에 있는 요소를 i로 불러오기
        for j in i:     # 요소안에 문자열을 문자로 쪼갠 문자 j
            if k == j:
                var += e_list[i]
print(var)