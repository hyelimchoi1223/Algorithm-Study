def add_two_elements(iterator):
    result = 0
    for i in range(0, len(iterator), 2):
        if i+1 == len(iterator):
            result += iterator[i]
        else:
            result += (iterator[i]*iterator[i+1])
    return result


N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))

minus = [x for x in numbers if 0 >= x]
minus.sort()
little = [x for x in numbers if x == 1]
large = [x for x in numbers if x >= 2]
large.sort(reverse=True)

result = sum(little)
result += add_two_elements(large)
result += add_two_elements(minus)
print(result)
