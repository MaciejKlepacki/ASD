# Złozoność czasowa: O(n log(n))
# Złozoność pamięciowa: O(1)
def heap_sort(T):
    n=len(T)
    build_heap(T)
    for i in range(n-1, 0, -1):
        T[0], T[i] = T[i], T[0]
        heapify(T, i, 0)
    return T

def build_heap(T):
    n=len(T)
    for i in range(parent(n-1), -1, -1):
        heapify(T, n, i)

def heapify(T, n, i):
    l=left(i)
    r=right(i)
    if l<n and T[l]>T[i]:
        largest=l
    else:
        largest=i
    if r<n and T[r]>T[largest]:
        largest=r
    if largest!=i:
        T[i], T[largest] = T[largest], T[i]
        heapify(T, n, largest)
def left(i):
    return 2*i+1
def right(i):
    return 2*i+2
def parent(i):
    return (i-1)//2

print(heap_sort([1,5,2,7,4,2,3,4]))