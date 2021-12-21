from itertools import permutations

# 1차 시도
# def solution(phone_book):
#     answer = True
#     if len(phone_book) == 1:
#         return answer
#     for i in range(len(phone_book)):
#         temp_phone = [x for x in phone_book if phone_book[i] != x]
#         for phone in temp_phone:
#             if phone.startswith(phone_book[i]) == True:
#                 answer = False
#                 return answer
#     return answer

# 2차 시도
# def solution(phone_book):
#     answer = True
#     if len(phone_book) == 1:
#         return answer

#     for x, y in permutations(phone_book, 2):
#         if y.startswith(x) == True:
#             answer = False
#             return answer
#     return answer

# 3차 시도
def solution(phone_book):
    answer = True
    if len(phone_book) == 1:
        return answer

    phone_book = sorted(phone_book)

    for i in range(len(phone_book) - 1):
        if phone_book[i + 1].startswith(phone_book[i]) == True:
            return False

    return answer


# 접두어가 있으면 False, 없으면 True
