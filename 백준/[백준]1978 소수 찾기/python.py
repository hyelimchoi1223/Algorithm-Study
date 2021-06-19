count = int(input())
num = list(map(int, input().split()))
if 1 in num:    
    num.remove(1)
result = 0
for _ in num:    
    temp = [i for i in range(1, _+1) if _%i==0]
    temp.remove(1)
    if _ in temp:
        temp.remove(_)
    if temp.__len__()==0:
        result += 1

print(result)