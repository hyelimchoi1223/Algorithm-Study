def sugarbag_min(n):
    bag_5 = n // 5
    if n % 5 == 0:
        return bag_5
    bag_3 = (n % 5)//3
    if (n % 5) % 3 == 0:
        print("5*{}+3*{}".format(bag_5, bag_3))
        return bag_5 + bag_3
    bag_3 += 1
    print("5*{}+3*{}".format(bag_5, bag_3))
    return bag_5+bag_3


while True:
    N = int(input())
    if N == -1:
        break
    predict_min = sugarbag_min(N)

    test = N//5
    if N % 5 != 0:
        test += N//3
        if (N % 5) % 3 == 0:
            test += 1
    if N % 3 == 0:
        test = N

    if predict_min > test:
        print(-1)
    else:
        print(predict_min)
