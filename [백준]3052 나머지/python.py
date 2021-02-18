values = []
for _ in range(1, 11):
    values.append(int(input())%42)
result = []
for _ in values:    
    if result.__contains__(_) == False:
        result.append(_)    
print(result.__len__())
