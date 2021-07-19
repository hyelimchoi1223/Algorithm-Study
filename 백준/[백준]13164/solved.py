N, K = map(int, input())
students = list(map(int, input().split()))
students.sort()

test = [x for i in range(N // K)
