def sort(array):
    if isinstance(array, list) is False:
        raise TypeError("array must be a list")

    if len(array) == 1:
        return array

    for i in range(0, len(array)):
        for j in range(len(array) - 1):
            right = array[j + 1]
            left = array[j]

            if left > right:
                array[j] = right
                array[j + 1] = left

    return array


print(sort([0]))
print(sort([2, 1, 3, 4, 5, 6, 7, 8, 9, 10]))
