import numpy as np
basket = []
global_board = []


def moves_doll(board, move):
    global global_board
    global basket
    for idx, pick in enumerate(global_board[move-1]):
        if pick == 0:
            continue
        value = global_board[move-1].pop(idx)
        basket.append(value)
        break


def destory_doll():
    global basket
    if len(basket) < 2:
        return False

    if basket[-1] == basket[-2]:
        basket.pop(-1)
        basket.pop(-1)
        return True
    return False


def solution(board, moves):
    global global_board
    global_board = np.array(board).T.tolist()

    answer = 0
    for m in moves:
        moves_doll(board, m)
        print(f'before {basket}')
        if destory_doll() == True:
            answer += 1
            print(f'after {basket}')
    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))
