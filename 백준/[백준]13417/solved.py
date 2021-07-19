from itertools import permutations
test_case = int(input())
for i in range(test_case):
    N = int(input())
    alphabet = input().split()
    all_value = list(permutations(alphabet, N))
    all_value.sort()
    print(all_value[0])
