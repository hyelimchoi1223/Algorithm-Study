N = int(input())

if N == 1:
    print("")
else:
    num = 2
    while True:
        if N // num == 0:
            break

        if N % num != 0:
            num += 1
        else:
            print(num)
            N = N // num
