# Złozoność czasowa: O(n*log(n))

def merge_sort(T):
    if len(T) <= 1:
        return T
    mid = len(T)//2
    left = merge_sort(T[:mid])
    right = merge_sort(T[mid:])
    return descending_merge(left, right)

def descending_merge(left, right):
    # Prealokujemy listę o ustalonym rozmiarze
    result = [None] * (len(left) + len(right))
    l = r = index = 0
    while l < len(left) and r < len(right):
        if left[l] >= right[r]:  # Zmieniono warunek na malejący porządek
            result[index] = left[l]
            l += 1
        else:
            result[index] = right[r]
            r += 1
        index += 1
    # Przepisujemy pozostałe elementy lewej tablicy
    while l < len(left):
        result[index] = left[l]
        l += 1
        index += 1
    # Przepisujemy pozostałe elementy prawej tablicy
    while r < len(right):
        result[index] = right[r]
        r += 1
        index += 1
    return result