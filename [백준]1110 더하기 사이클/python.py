value = input().zfill(2)
origin = value
count = 0
while True:    
    temp = int(value[0])+int(value[1])       
    value = value[1]+str(temp).zfill(2)[1]
    count +=1
    if value == origin:
        break       
print(count)