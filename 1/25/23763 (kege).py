def f(x):
    deli = []
    for d in range(2, x):
        if x % d == 0:
            deli.append(d)
    if len(deli) == 0:
        return 0
    if len(deli) > 0:
        return min(deli) + max(deli)


cnt = 0
for i in range(800_001, 1_000_000):
    m = f(i)
    if m % 10 == 4:
        print(i, m)
        cnt = cnt + 1
    if cnt == 5:
        break
