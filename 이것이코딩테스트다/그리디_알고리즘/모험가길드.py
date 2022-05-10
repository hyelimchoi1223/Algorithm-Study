N = int(input())
adventure = map(int, input().split())
adventure = sorted(adventure)

result = 0
current_group_cnt = 0
for u in adventure:
    current_group_cnt += 1
    if current_group_cnt >= u:
        result += 1
        current_group_cnt = 0

print(result)
