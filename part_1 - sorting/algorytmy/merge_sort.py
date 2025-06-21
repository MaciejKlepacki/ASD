# Złozoność czasowa: O(nlogn)
# Złozoność pamięciowa: O(n)

def merge_sort(T):
    if len(T) <= 1:
        return T
    mid = len(T)//2
    left = merge_sort(T[:mid])
    right = merge_sort(T[mid:])
    return merge(left, right)

def merge(left, right):
    result = [None] * (len(left) + len(right))
    l = r = index = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[index] = left[l]
            l += 1
        else:
            result[index] = right[r]
            r += 1
        index += 1
    while l < len(left):
        result[index] = left[l]
        l += 1
        index += 1
    while r < len(right):
        result[index] = right[r]
        r += 1
        index += 1
    return result

print(merge_sort(['asdfasf','asdfa']))