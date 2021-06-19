array=[]
for _ in range(1, 10):
    array.append(int(input()))
temp = array.copy()
temp.sort()
max =temp[temp.__len__()-1]
print(max)
print(array.index(max)+1)