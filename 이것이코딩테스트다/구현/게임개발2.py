N, M = map(int, input().split())
A, B, d = map(int, input().split())
# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn_left():
    global d
    d = (d + 1) % 4


board = []
for n in range(N):
    board.append(input().split())

result = 0
count = 0
while True:
    turn_left()
    nx = A + dx[d]
    ny = B + dy[d]

    if board[nx][ny] == "0":
        A = nx
        B = ny
        board[A][B] = "1"
        result += 1
        count = 0
        continue
    else:
        count += 1

    if count == 4:
        nx = A - dx[d]
        ny = B - dy[d]

        if board[nx][ny] == "0":
            A = nx
            B = ny
        else:
            break
        count = 0
print(result)
