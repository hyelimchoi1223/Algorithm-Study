T = int(input())
A, B, C = 5*60, 1*60, 10
err_result = 0
result = [0, 0, 0]
while True:
    if T <= 0:
        break
    if T >= A:
        T -= A
        result[0] += 1
    elif T >= B:
        T -= B
        result[1] += 1
    elif T >= C:
        T -= C
        result[2] += 1
    else:
        T = -1
        err_result = -1

if T < 0:
    print(err_result)
else:
    print(*result, sep=' ')
