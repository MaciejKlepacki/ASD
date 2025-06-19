
from egzP2btesty import runtests
from math import log10

def kryptograf( D, Q ):
    # O(nm)
    for i in range(len(D)):
        D[i] = D[i][::-1]
    # O(qm)
    for i in range(len(Q)):
        Q[i] = Q[i][::-1]
    # O(nm*log(nm))
    D.sort()
    multipier = 1
    # O(qm*log(n))
    for i in Q:
        lo = bin_serach_l(D, i)
        hi = bin_serach_r(D, i + '2')
        multipier *= hi - lo

    return log10(multipier)

# O(m*log(n))
def bin_serach_l(D, i):
    lo, hi = 0, len(D)
    while lo < hi:
        mid = (lo + hi) // 2
        if D[mid] < i:
            lo = mid + 1
        else:
            hi = mid
    return lo
# O(m*log(n))
def bin_serach_r(D, i):
    lo, hi = 0, len(D)
    while lo < hi:
        mid = (lo + hi) // 2
        if D[mid] <= i:
            lo = mid + 1
        else:
            hi = mid
    return lo



# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests = 3)