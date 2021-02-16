count = int(input())
result = []
for _ in range(1, count+1):
    X, Y = input().split()
    result.append(int(X)+int(Y))
    
for _ in result:
    print(_)