C = int(input())

max_cnt = 0
for c in range(C):
    text = input()
    for_cnt = text.count("for")
    while_cnt = text.count("while")
    cnt = for_cnt + while_cnt
    if max_cnt < cnt:
        max_cnt = cnt

print(max_cnt)
