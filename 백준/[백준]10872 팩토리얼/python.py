N = int(input())
if N == 0:
    print(1)
else:
    result = 1
    while True:
        if N == 0:
            break
        result *= N
        N -= 1

    print(result)
