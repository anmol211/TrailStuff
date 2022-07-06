import collections


def distinct_elements(arr: list, k):
    for i in range(len(arr)-k+1):
        print(len(set(arr[i:i+k])))

arr = [1,2,1,3,4,3,3]
distinct_elements(arr,4)

