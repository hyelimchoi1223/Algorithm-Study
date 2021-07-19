n = int(input())
students = list(map(int, input().split()))

students.sort()

result_min = 0
for i in range(n):
    temp = students[i] + students[-(i+1)]
    if not result_min:
        result_min = temp
    elif temp < result_min:
        result_min = temp

print(result_min)
