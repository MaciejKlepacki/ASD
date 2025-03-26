def selectionSort(array):
    sorted_array = array[:]
    size = len(sorted_array)
    for ind in range(size):
        min_index = ind
        for j in range(ind + 1, size):
            if sorted_array[j] < sorted_array[min_index]:
                min_index = j
        (sorted_array[ind], sorted_array[min_index]) = (sorted_array[min_index], sorted_array[ind])
    return sorted_array

print(selectionSort([3, 5, 1, 6, 4, 8, 2, 3, 1]))