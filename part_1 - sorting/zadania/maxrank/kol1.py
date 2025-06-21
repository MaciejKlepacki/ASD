from kol1testy import runtests

#  quick sort
def quick_sort(T, l, r):
    if l<r:
        p=partition(T, l, r)
        quick_sort(T, l, p-1)
        quick_sort(T, p+1, r)
    return T

def partition(T, l, r):
    x=T[r]
    i=l-1
    for j in range(l, r):
        if T[j]<=x:
            i+=1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[r] = T[r], T[i+1]
    return i+1


def maxrank(T):
    n = len(T)
    for i in range(n):
        T[i] = (T[i], i)
    quick_sort(T, 0, n - 1)
    max_rank = 0
    i = n - 1
    while i > max_rank:
        idx = T[i][1]
        while i > 0 and T[i - 1][0] == T[i][0]:
            i -= 1
            if T[i][1] > idx:
                idx = T[i][1]

        rank = idx - (n - i - 1)
        if rank > max_rank:
            max_rank = rank
        
        i -= 1
    
    return max_rank

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )