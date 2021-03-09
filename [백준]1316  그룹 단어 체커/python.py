from itertools import groupby
def checkgroup(word):
    group = [key for key, item in groupby(word)]
    values =[(k, [i for i in range(len(word)) if word[i] == k]) for k in group]

    groupword = 0
    for items in values:
        if items[1].__len__() == 0:
            groupword += 1
            continue        
        for index in range(1, items[1].__len__()):
            if items[1][index]-items[1][index-1] >1:
                groupword = 0
                return groupword
        groupword += 1
    return groupword    
        
        
        
count = int(input())
words = [input() for _ in range(count)]
result = 0
for _ in words:
    groupcount = checkgroup(_)
    if groupcount != 0:
        result+=1
    
print(result)
        
    

        
        
    
            