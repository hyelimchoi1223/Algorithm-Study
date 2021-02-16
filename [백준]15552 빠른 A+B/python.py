import sys
count = int(sys.stdin.readline())
for _ in range(1, count+1):
    X, Y = sys.stdin.readline().split()
    print(int(X)+int(Y))