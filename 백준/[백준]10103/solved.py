N = int(input())
A, B = 100, 100
for n in range(N):
    a, b = map(int, input().split(" "))
    if a < b:
        A = A - b
    elif a > b:
        B = B - a
    else:
        continue

print(A)
print(B)
