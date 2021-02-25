count = int(input())
word = ""
for _ in range(3):
    word += input()
my_tuple = []
firstchar = word[0]
charCnt = 1

index = 0
for i in word:
    print("1."+i)
    index += 1
    for j in word[index::]:
        print(j)
        
        
    
            