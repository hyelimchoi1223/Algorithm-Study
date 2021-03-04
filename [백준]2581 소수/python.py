def isMinority(value):
    result = [_ for _ in range(1, value+1) if value % _ == 0]
    result.remove(1)
    result.remove(value)
    return True if result.__len__() == 0 else False
    
M = int(input())
N = int(input())
num_array = [_ for _ in range(M, N+1) if isMinority(_) is True]

if num_array.__len__() == 0:
    print(-1)
else:
    print(sum(num_array))
    print(min(num_array))
