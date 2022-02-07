T = int(input())

for t in range(T):
    N = int(input())
    yangjojang = {}
    for n in range(N):
        S, L = input().split(" ")
        L = int(L)
        yangjojang[S] = L

    print(sorted(yangjojang, key=lambda x: yangjojang[x], reverse=True)[0])
