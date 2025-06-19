from humanfriendly.terminal import output
import bisect
from egzP2btesty import runtests
from math import log10

def radix_sort(tab, x):
    if x == -1:
        return tab

    it = x
    output_0 =[]
    output_1 = []

    for i in tab:
        if len(i) <= it:
            output_0 = [i] + output_0
        elif i[it] == '0':
            output_0.append(i)
        else:
            output_1.append(i)
    return radix_sort(output_0 + output_1, x-1)


def kryptograf( D, Q ):
    maxi = 0
    for i in range(len(D)):
        D[i] = D[i][::-1]
        maxi = max(len(D[i]), maxi)
    for i in range(len(Q)):
        Q[i] = Q[i][::-1]

    D = radix_sort(D, maxi)

    output = 0
    # O(qm*log(n))
    for i in Q:
        lo = bin_serach_l(D, i)
        hi = bin_serach_r(D, i + '2')
        output += log10(hi-lo)

    return output


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
runtests(kryptograf, all_tests = 2)