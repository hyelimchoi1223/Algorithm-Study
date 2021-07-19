N = int(input())

count = 0
if N <= 3*5 and (N % 3 == 0 or N % 5 == 0):
    if N % 3 == 0:
        count = N // 3
    elif N % 5 == 0:
        count = N // 5
else:
    while True:
        if N < 0:
            count = -1
            break
        elif N == 0:
            break
        if N % 5 == 0 or N % 3 != 0:
            count += 1
            N -= 5
        elif N % 3 == 0:
            count += 1
            N -= 3
        else:
            count = -1


print(count)
