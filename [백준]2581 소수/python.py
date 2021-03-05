def isMinority(value):
    if value == 1:
        return True
    result = [_ for _ in range(2, value) if value % _ == 0]
    print(value, result)
    return True if result.__len__() == 0 else False
    
M = int(input())
N = int(input())
num_array = [_ for _ in range(M, N+1) if isMinority(_) is True]

if num_array.__len__() == 0:
    print(-1)
else:
    print(sum(num_array))
    print(min(num_array))
