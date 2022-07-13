"""
내가 생각한 풀이 : 이동하는 함수(move)와 돌리는 함수(rotate)를 활용해 가능성을 모두 탐색
하지만 각도를 입력으로 받고 돌리는 기능을 생각하다 보니 rotate 함수 구현을 하지 못함
제안된 풀이 : 자물쇠를 기존 크기보다 3배 크게 생각을 하고, rotate함수는 90도만 도는 함수로 만듦.
전체 자물쇠를 탐색하고, rotate를 해가며 맞는 위치를 찾아감
"""


def rotate_90(key):
    m = len(key)
    temp = [[0] * m for _ in range(m)]

    for i, row in enumerate(key):
        for j, col in enumerate(row):
            temp[j][m - i - 1] = col
    return temp


def check(newlock):
    lock_length = len(newlock) // 3
    for i in range(lock_length, lock_length * 2):
        for j in range(lock_length, lock_length * 2):
            if newlock[i][j] != 1:
                return False

    return True


def solution(key, lock):
    n = len(lock)
    m = len(key)
    temp = [[0] * (n * 3) for _ in range(n * 3)]

    # lock 초기화
    for i, row in enumerate(lock):
        for j, col in enumerate(row):
            temp[i + n][j + n] = col

    for _ in range(4):
        key = rotate_90(key)

        for x in range(n * 2):
            for y in range(n * 2):

                for i in range(m):
                    for j in range(m):
                        temp[x + i][y + j] += key[i][j]

                if check(temp) == True:
                    return True

                # 자물쇠에서 빼내기
                for i in range(m):
                    for j in range(m):
                        temp[x + i][y + j] -= key[i][j]

    return False


v_key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
v_lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(v_key, v_lock))
