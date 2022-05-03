########## 재귀함수로 해결
def fibonacci(n):
    if n == 1 or n == 2:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))


########### 메모이제이션으로 해결

cache = [0] * 100


def fibonacci2(n):
    if n == 1 or n == 2:
        return 1

    if cache[n] == 0:
        cache[n] = fibonacci2(n - 1) + fibonacci2(n - 2)

    return cache[n]


print(fibonacci2(99))

########### Bottom-up
def fibonacci3(n):
    cache = [0] * 100

    cache[1] = 1
    cache[2] = 1

    for i in range(3, n + 1):
        cache[i] = cache[i - 1] + cache[i - 2]

    return cache[n]


print(fibonacci3(99))
