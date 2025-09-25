def f(x):
    is_ok = False
    min_del = None
    for d in range(2, x):
        if x % d == 0 and d % 10 == 7 and d != x and d != 7:
            is_ok = True
            min_del = d
            break
    return is_ok, min_del


cnt = 0
for i in range(1_125_001, 1_125_001 + 1_125_001):
    if f(i)[0] == True:
        print(i, f(i)[1])
        cnt += 1
    if cnt == 5:
        break
