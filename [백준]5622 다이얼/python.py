dial_dic = {1:"", 2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL", 6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ", 0:""}
value = input()
result = 0
for _ in value:
    num = [k for k, v in dial_dic.items() if _ in v]
    result += (num[0]+1)    
print(result)