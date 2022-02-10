V = int(input())
score = list(input())

a = score.count("A")
b = score.count("B")

if a > b:
    print("A")
elif a < b:
    print("B")
else:
    print("Tie")
