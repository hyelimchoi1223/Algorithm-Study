count = int(input())
for _ in range(count):
    H, W, N = map(int, input().split())
    x = (N // H)+1
    y = (N % H)
    if y == 0:
        x = N // H
        y = H
    
    print('{}{}'.format(y, '{:02d}'.format(x)))