# 1 способ
for A in range(1, 1000):
    if all(((not (x % A == 0)) <= ((x % 28 == 0) <= (not (x % 49 == 0)))) for x in range(1, 1000)):
        print(A)

# 2 способ
for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if ((not (x % A == 0)) <= ((x % 28 == 0) <= (not (x % 49 == 0)))) == False:
            flag = False
            break
    if flag:
        print(A)
