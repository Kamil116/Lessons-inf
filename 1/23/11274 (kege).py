def f(x):
    if x > 42:
        return 0
    if x == 42:
        return 1
    return f(x + 4) + f(x * 2)


print(f(13))
