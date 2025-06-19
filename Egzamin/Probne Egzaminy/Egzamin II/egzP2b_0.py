from egzP2btesty import runtests
from math import log10

def kryptograf( D, Q ):
    multipiler = 1
    for q in Q:
        counter = 0
        for d in D:
            c = len(d) - len(q)
            if q == d[c:]:
                counter += 1
        multipiler *= counter
    return log10(multipiler)

# Zmień all_test na:
# 0 - Dla małych testów
# 1 - Dla złożoności akceptowalnej
# 2 - Dla złożoności dobrej
# 3 - Dla złożoności wzorcowej
runtests(kryptograf, all_tests = 0)