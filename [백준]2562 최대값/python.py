def algorithm(array):
    temp = array.copy()
    temp.sort()
    print("temp:",temp)
    print("array:",array)
    max =temp[temp.__len__()-1]
    print(max)
    print(array.index(max)+1)
    print("----")
# array=[]
# for _ in range(1, 10):
#     array.append(int(input()))
import random
for _ in range(1, 100):
    testData=[random.randrange(1,100) for _ in range(10)]
    print(testData)
    algorithm(testData)


