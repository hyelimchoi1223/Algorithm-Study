goal = int(input())
temp = 0
index = 0
while True:
    if temp >= goal:
        break    
    index +=1
    temp = (index)*(index+1)//2

pos = goal-(index)*(index-1)//2 
if index % 2== 0:
    num_array = [(_, (index+1)-_) for _ in range(1, index+1, 1)]
else:
    num_array = [(_, index-(_-1)) for _ in range(index, 0, -1)]

value = num_array[pos-1]
print("{}/{}".format(value[0], value[1]))
