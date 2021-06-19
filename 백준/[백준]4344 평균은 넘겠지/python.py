def getmean(iterable):
    sum = 0
    for _ in iterable:
        sum += _
    return sum/iterable.__len__()


loopCount = int(input())

for _ in range(0, loopCount):
    values = list(map(float, input().split()))
    # 첫번째 데이터 = 학생수  -> pop을 이용해 첫번째 데이터만 꺼냄
    num_student = values.pop(0)
    # 평균 구하는 함수를 만들어 사용
    mean = getmean(values)
    # 줄 수를 간소화 하기 위해 filter와 lambda식을 사용
    count = list(filter(lambda x: x > mean, values)).__len__()
    # 소수 셋째자리까지 구하기 위해 format 사용
    # rount를 사용했을 떄 자리수가 안맞아도 0이면 표시를 안함
    print("{}%".format(format(count/num_student*100, '.3f')))
