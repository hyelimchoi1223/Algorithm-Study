# 가장 높은 숫자가 쓰인 카드 한 장을 뽑는 게임
# 1. 카드들은 N X M 형태로 놓여 있음. (M은 열의 개수)
# 2. 먼저 뽑고자 하는 카드 포함되어 있는 행 선택
# 3. 선택된 행에 포함된 카드들 중 가장 낮은 숫자의 카드를 뽑아야 함.
# 4. 처음 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을 것을 고려하여
# 최종적으로 가장 높은 숫자의 카드를 뽑을 수 있도록 전략을 세워야 한다.

N, M = map(int, input().split())
cards = []

for i in range(N):
    cards.append(list(map(int, input().split())))

max_card = 0
for item in cards:
    if max_card < min(item):
        max_card = min(item)
print(max_card)
