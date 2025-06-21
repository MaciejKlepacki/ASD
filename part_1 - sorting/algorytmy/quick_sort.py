# Złozoność czasowa:
#   - pesymistyczna: O(n^2)
#   - średnia: O(n log(n))
# Złozoność pamięciowa: O(n)

def quick_sort(T, l, r): # Zwykle l = 0, r = len(T)-1
    if l<r:
        p=partition(T, l, r)    # funkcja partition zwrana nam indeks pivota, po ktorego lewej stronie elementy są mnijesze lub rowne niemu, a po prawej wieksze od niego
        quick_sort(T, l, p-1)
        quick_sort(T, p+1, r)  # rekurencyjnie wywolujemy quicksorta na tych podzielonych częćciach względem pivota
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