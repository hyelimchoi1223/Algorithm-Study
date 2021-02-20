import time
num_list = list(range(1, 10001))
array = []


def d(n):
    my_sum = n
    my_sum += sum(list(map(int, str(n))))
    if my_sum > 10000:
        return
    if num_list.__contains__(my_sum):
        num_list.remove(my_sum)
    d(my_sum)


start = time.time()
for _ in num_list:
    d(_)
    print(_)
print(time.time()-start)
