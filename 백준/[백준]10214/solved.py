T = int(input())
for t in range(T):
    Y, K = 0, 0
    for i in range(9):
        y, k = map(int, input().split(" "))
        Y += y
        K += k

    if Y > K:
        print("Yonsei")
    elif Y < K:
        print("Korea")
    else:
        print("Draw")
