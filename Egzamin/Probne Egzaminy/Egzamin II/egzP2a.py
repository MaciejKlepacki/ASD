from unittest.mock import right

from egzP2atesty import runtests

def zdjecie(T, m, k):
    sorted_T = merge_sort(T)[::-1]

    F = [[0 for _ in range(m+k-1-i) ] for i in range(m)]

    t = 0
    for i in range(m):
        for j in range(m+k-1-i):
            F[i][j] = sorted_T[t]
            t += 1
    t = 0
    for j in range(m+k-1):
        for i in range(m):
            if j < m+k-1-i:
                T[t] = F[i][j]
                t += 1

    return None

def merge_sort(T):
    if len(T) <= 1:
        return T
    mid = len(T) // 2
    left = merge_sort(T[:mid])
    right = merge_sort(T[mid:])
    return merge(left, right)

def merge(left, right):
    result = [None] * (len(left) + len(right))
    l = r = index = 0
    while l < len(left) and r < len(right):
        if left[l][1] <= right[r][1]:
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

runtests ( zdjecie, all_tests=False )