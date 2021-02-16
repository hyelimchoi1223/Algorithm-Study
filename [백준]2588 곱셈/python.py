value1=input()
value2=input()

result = 0
index = 0
for _ in value2[::-1]:    
    temp = int(value1)*int(_)
    print(temp)
    result += temp*(10**index)
    index += 1

print(result)