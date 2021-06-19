count = int(input())
for _ in range(1, count+1):
    answer = input()
    score = 0
    result = 0
    for item in answer:
        if item == 'O':
            score += 1
        else:
            score = 0
        result += score
    print(result)
