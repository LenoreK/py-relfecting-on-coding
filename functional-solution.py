def flatten_and_sort(array):
    arr = []
    for item in array:
        for i in item:
            arr.append(i)
    return sorted(arr)

print(flatten_and_sort([[12, 55, 1], [2, 33, 4], [88, 44, 3]]))