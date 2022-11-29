from functools import partial


def sum(a, b):
    return a + b


d = partial(sum, b=1)
print(d(2))

d = {'a' : 1}
d.update([('b',2)])
print(d)


for i, j in zip([1,2,3], [1,2,3,4,5]):
    print(i,j)