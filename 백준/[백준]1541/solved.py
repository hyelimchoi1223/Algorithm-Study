N = input()


def sum_func(src):
    numbers = list(map(int, src.split('+')))
    return sum(numbers)


result = 0
for index, value in enumerate(N.split('-')):
    if index == 0:
        result = sum_func(value)
        continue

    result -= sum_func(value)

print(result)
