import time
num_list = list(range(1, 10001))
my_array = []


def d(n):
    global my_array
    my_sum = n
    my_sum += sum(list(map(int, str(n))))
    if my_sum > 10000:
        return
    my_array.append(my_sum)
    d(my_sum)


for _ in num_list:
    d(_)

my_array = list(set(my_array))
result = [a for a in num_list if a not in my_array]
print("\n".join(map(str, result)))
