N, M = map(int, input().split())
A, B, d = map(int, input().split())

board = []
for n in range(N):
    board.append(input().split())
result = 0
while True:
    board[A][B] = "9"
    count = 0
    while True:
        count += 1
        d = (d + 1) % 4
        if count >= 4:
            count = 0
            A = A - 1
            if board[A][B] == "1":
                d = 5
                break

        if d == 1 and (board[A][B - 1] != "1" and board[A][B - 1] != "9"):
            break
        elif d == 2 and (board[A + 1][B] != "1" and board[A + 1][B] != "9"):
            break
        elif d == 3 and (board[A][B + 1] != "1" and board[A][B + 1] != "9"):
            break
        elif d == 0 and (board[A - 1][B] != "1" and board[A - 1][B] != "9"):
            break

        # 네 방향 모두 갈 수 없으면 바라보ㅡㄴ 방향을 유지한 채로 하난 뒤로가고 1단계로 돌아감.
        # 뒤쪽이 바다이면 움직임을 멈춘다

    if d == 1:
        B = B - 1
        result += 1
    elif d == 2:
        A = A + 1
        result += 1
    elif d == 3:
        B = B + 1
        result += 1
    elif d == 0:
        A = A - 1
        result += 1
    else:
        break

print(result)
