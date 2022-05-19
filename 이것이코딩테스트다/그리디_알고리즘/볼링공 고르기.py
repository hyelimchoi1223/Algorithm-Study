# 해결방법
# 본인과 같은 수를 제외한 나머지의 개수를 합한다.
N, M = map(int, input().split())
balls = list(map(int, input().split()))

result = 0
for idx, b in enumerate(balls):
    different = len([i for i in balls[idx:] if i != b])
    result += different

print(result)
