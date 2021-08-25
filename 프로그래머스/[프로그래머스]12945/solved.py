def Fibonacci(num):
    if num == 0 or num == 1:
        return num
    return (Fibonacci(num-1) % 1234567 + Fibonacci(num-2) % 1234567) % 1234567


def Fibonacci2(num):
    bottomup = []
    bottomup.append(0)
    bottomup.append(1)

    for i in range(2, num+1):
        bottomup.append((bottomup[i-1] % 1234567 + bottomup[i-2] %
                         1234567) % 1234567)

    return bottomup[num]


def solution(n):
    answer = Fibonacci2(n)
    return answer


# int의 자료형은 -2,147,483,648 ~ 2,147,483,647
# 문제가 1234567로 나눈 나머지를 출력하라고 하는 것.
# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.
print(solution(2))
print(solution(3))
print(solution(4))
print(solution(5))
print(solution(6))
