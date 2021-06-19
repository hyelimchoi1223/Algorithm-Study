alpha_dic = dict([(i, 0) for i in range(97, 123)])
value = input()
for key in alpha_dic.keys():
    alpha_dic[key] = value.find(chr(key))
print(" ".join(map(str, alpha_dic.values())))
