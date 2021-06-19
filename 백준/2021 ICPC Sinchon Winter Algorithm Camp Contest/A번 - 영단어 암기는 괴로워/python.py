N, M = map(int, input().split())

list_temp = [input() for _ in range(N)]
# word_dic = dict([(_, list_temp.count(_))
#                  for _ in list(set(list_temp))if len(_) >= M])
# word_dic = dict(sorted(word_dic.items(), key=(
#     lambda x: (-x[1], -len(x[0]), x[0]))))
# print("\n".join(list(word_dic.keys())))
word_dic = [(_, list_temp.count(_))
            for _ in list(set(list_temp))if len(_) >= M]
word_dic = sorted(word_dic, key=(
    lambda x: (-x[1], -len(x[0]), x[0])))
print("\n".join([_[0] for _ in word_dic]))
