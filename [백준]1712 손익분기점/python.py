A,B,C = map(int, input().split())
count = A//(C-B)
if C-B <=0:
    print(-1)
elif (C*count)-(A+B*count) >= 0:
        print(count+1)