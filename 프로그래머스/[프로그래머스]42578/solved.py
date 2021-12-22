import math


def coefficient(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


# 1차 풀이
# def solution(clothes):
#     answer = 0

#     spy_clothes = {}
#     for data in clothes:
#         cloth = []
#         if data[1] in spy_clothes.keys():
#             cloth = spy_clothes[data[1]]
#             cloth.append(data[0])
#         else:
#             spy_clothes[data[1]] = [data[0]]

#     array_length = 0
#     for kind, cloth in spy_clothes.items():
#         # 부위별 1개씩 나오는 경우 계산
#         array_length += len(cloth)
#     answer += array_length

#     if len(spy_clothes.keys()) > 1:
#         all_coefficient = 1  # 모든 부위별로 1개씩 나오는 경우 계산
#         for kind, cloth in spy_clothes.items():
#             all_coefficient *= coefficient(len(cloth), 1)

#         answer += all_coefficient

#     return answer


# 2차 풀이
def solution(clothes):
    answer = 1
    clothes = make_hash_table(clothes)
    key_length = len(clothes.keys())
    for key, item in clothes.items():
        answer *= coefficient(len(item), 1) * (coefficient(len(item), 1) + 1)

    answer -= 1
    return answer


def make_hash_table(clothes):
    spy_clothes = {}
    for data in clothes:
        cloth = []
        if data[1] in spy_clothes.keys():
            cloth = spy_clothes[data[1]]
            cloth.append(data[0])
        else:
            spy_clothes[data[1]] = [data[0]]

    return spy_clothes

