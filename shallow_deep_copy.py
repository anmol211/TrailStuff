import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
deep_list = copy.deepcopy(old_list)
shallow_list = copy.copy(old_list)

old_list[1][0] = 'BB'
old_list.append([4, 4, 4])

print("Old list:", old_list)
print("Deep list:", deep_list)
print("Shallow List", shallow_list)