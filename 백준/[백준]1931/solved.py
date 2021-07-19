N = int(input())
meeting = []

for i in range(N):
    meeting.append(tuple(map(int, input().split())))

meeting.sort(key=lambda x: (x[1], x[0]))
# 끝나는 시간으로 오름차순 정렬하되 끝나는 시간이 같다면 시작시간을 오름차순 정렬 해야 함.

count = 0
end_time = -1
for start, end in meeting:
    if end_time == -1:
        end_time = end
        count = 1
    elif end_time <= start:
        count += 1
        end_time = end


print(count)
