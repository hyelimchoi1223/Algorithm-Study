plates = list(input())
height = 0
before = ""
for idx, p in enumerate(plates):
    if idx == 0:
        height += 10
        before = p
        continue

    if before == p:
        height += 5
    else:
        height += 10

    before = p

print(height)
