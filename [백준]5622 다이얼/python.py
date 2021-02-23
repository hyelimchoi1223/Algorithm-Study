dial = [-1,-1,1,('A','B','C'),('D','E','F'),('G','H','I'),('J','K','L'),('M','N','O'),('P','Q','R','S'),('T','U','V'),('W','X','Y','Z'),0]
dial_dic = {1:"", 2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL", 6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ", 0:""}
value = input()
result = 0
for _ in value:
    num = [k for k, v in dial_dic.items() if _ in v]
    result += (num[0]+1)    
print(result)