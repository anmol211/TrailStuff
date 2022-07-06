
def infinite_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

g = infinite_fib()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
