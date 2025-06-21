def merge_sort_with_index(arr):
    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i][0] <= right[j][0]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def merge_sort(arr_with_index):
        if len(arr_with_index) <= 1:
            return arr_with_index
        mid = len(arr_with_index) // 2
        left = merge_sort(arr_with_index[:mid])
        right = merge_sort(arr_with_index[mid:])
        return merge(left, right)

    arr_with_index = [(value, index) for index, value in enumerate(arr)]
    return merge_sort(arr_with_index)

# Example usage:
arr = [4, 2, 7, 1]
print(merge_sort_with_index(arr))
# Output: [(1, 3), (2, 1), (4, 0), (7, 2)]
