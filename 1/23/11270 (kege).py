def f(x, y):
    if x == y:
        return 1
    if x == 32:
        return 0
    if x < y:
        return 0
    return f(x - 1, y) + f(x - 5, y)


print(f(42, 23) * f(23, 22) * f(22, 9))
