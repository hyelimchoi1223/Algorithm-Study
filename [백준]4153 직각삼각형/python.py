while True:
    x = list(map(int, input().split()))
    if x[0] == 0 and x[1]==0 and x[2]==0:
        break
    index=x.index(max(x))
    c = x[index]**2
    x.pop(index)
    ab = sum([_ **2 for _ in x])
    if c==ab:
        print("right")
    else:
        print("wrong")
    