cnt = int(input())
numbers = []
for i in range(cnt):
    number = int(input())
    numbers.append(number)

numbers.sort()
for num in numbers:
    print(num)
