def infinite_fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


g = infinite_fib()
for _ in range(5):
    print(next(g))
