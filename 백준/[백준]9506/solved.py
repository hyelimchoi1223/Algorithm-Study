while True:
    n = int(input())
    if n == -1:
        break
    p = []
    for i in range(1, n):
        if n % i != 0:
            continue
        p.append(i)

    if sum(p) == n:
        print(f"{n} = {' + '.join(map(str,p))}")
    else:
        print(f"{n} is NOT perfect.")
