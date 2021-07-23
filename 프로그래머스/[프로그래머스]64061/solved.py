import numpy as np
basket = []
global_board = np.array([])


def moves_doll(move):
    global global_board
    global basket

    for idx, item in enumerate(global_board[:, move-1]):
        if item == 0:
            continue
        basket.append(item)
        global_board[idx, move-1] = 0
        break


def destory_doll():
    global basket
    if len(basket) < 2:
        return 0

    if basket[-1] == basket[-2]:
        basket.pop(-1)
        basket.pop(-1)
        return 2
    return 0


def solution(board, moves):
    global global_board
    global_board = np.array(board)

    answer = 0
    for m in moves:
        moves_doll(m)
        answer += destory_doll()
    return answer
