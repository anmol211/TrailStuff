from functools import partial


def sum(a, b):
    return a + b


d = partial(sum, b=1)
print(d(2))

d = {'a' : 1}
d.update([('b',2)])
print(d)