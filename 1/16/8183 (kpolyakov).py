from functools import lru_cache


@lru_cache()
def fn(n):
    if n < 20:
        return n
    if n >= 20:
        return (n - 6) * fn(n - 7)


for i in range(1, 47865 + 1):
    fn(i)

print((fn(47872) - 290 * fn(47865)) / fn(47858))
