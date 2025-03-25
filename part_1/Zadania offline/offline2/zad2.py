# Maciej Klepacki
# Wykorzystanie merge_sorta do zliczenia łącznej liczby inwersji.
# Licznik inwersji zwiększa się, gdy  element z prawej tablicy jest mniejszy od tej z lewej.
# Z. czasowa: O(nlogn)
# Z. pamięciowa: O(n)

from zad2testy import runtests

def count_inversions(A):
    _, inversions = merge_sort(A)
    return inversions

def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = merge_sort(arr[:mid])
    right, inv_right = merge_sort(arr[mid:])
    merged, inv_merge = merge(left, right)
    return merged, inv_left + inv_right + inv_merge

def merge(left, right): 
    result = [0] * (len(left) + len(right))
    inversions = 0
    l = r = k = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            result[k] = left[l]
            l += 1
        else:
            result[k] = right[r]
            r += 1
            inversions += (len(left) - l)
        k += 1
    while l < len(left):
        result[k] = left[l]
        l += 1
        k += 1
    while r < len(right):
        result[k] = right[r]
        r += 1
        k += 1
    return result, inversions

# Odkomentuj by uruchomic duze testy
runtests( count_inversions, all_tests=True )

# Zakomentuj gdy uruchamiasz duze testy
# runtests( count_inversions, all_tests=False )