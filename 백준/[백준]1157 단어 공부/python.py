word = input().upper()
alphabet = [(_, word.count(_)) for _ in list(set(word))]
max_item = max(alphabet, key = lambda x: x[1])
same_count = [_ for _ in alphabet if max_item[1]==_[1]]
if same_count.__len__() >1:
    print("?")
else:
    print(same_count[0][0])