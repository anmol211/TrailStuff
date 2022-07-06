import array
import numpy as np

list_sample = [1, 2, 3, 4, 5, 6, 7]
a = array.array('i', list_sample)
print(a[3:])


def list_rotate(_list: list, rotation: int):
    n = len(_list)
    rotation = rotation % n
    return _list[rotation:] + _list[:rotation]


print(list_rotate(list_sample, 100))


def find_pair(_list: list, sum: int):
    n = len(_list)
    flag = False
    ar = np.array(_list)
    for i in range(n):
        ar1 = ar + _list[i]
        b = ar1 == sum
        if np.extract(b, ar1).size > 0:
            flag = True
            break
    return flag


print(find_pair([11, 15, 6, 8, 9, 10], 16))


def rotate_count(_list: list):
    n = len(_list)
    min_value = min(_list)
    ro_index = _list.index(min_value)
    return ro_index


print(rotate_count([15, 18, 2, 3, 6, 12]))
