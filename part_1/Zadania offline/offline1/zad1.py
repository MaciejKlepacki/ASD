# Maciej Klepacki
# W pierwszym etapie algorytm sortuje tablice merge_sortem. Potem zlicza ilość początkowych wyrazów, wliczając do tego równiez te odwrócone, które znajdowane są binary_searchem. Funkcja strong_string zwraca największą siłę.

from zad1testy import runtests


def strong_string(T):
    if len(T) == 0:
        return 0
    T = merge_sort(T)
    final_force = 1
    while len(T) != 0:
        force = 1
        acc = T[0]
        T.pop(0)
        while len(T) > 0 and T[0] == acc:
            force += 1
            T.pop(0)
        acc = acc[::-1]
        i = binary_search_first(T, acc)
        while i != -1 and i < len(T) and T[i] == acc:
            force += 1
            T.pop(i)
            i = binary_search_first(T, acc)
        if force > final_force:
            final_force = force
    return final_force

def binary_search_first(T, x):
    left, right = 0, len(T) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if T[mid] == x:
            result = mid
            right = mid - 1  # Continue searching in the left half
        elif T[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return result

def merge_sort(T):
    if len(T) > 1:
        mid = len(T) // 2
        left_half = T[:mid]
        right_half = T[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                T[k] = left_half[i]
                i += 1
            else:
                T[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            T[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            T[k] = right_half[j]
            j += 1
            k += 1

    return T

# Odkomentuj by uruchomic duze testy
# runtests(strong_string, all_tests=True)

# Zakomentuj gdy uruchamiasz duze testy
runtests(strong_string, all_tests=True)
# print(strong_string(['pies','mysz','kot','kogut','tok','seip','kot']))
# print(strong_string(['yrghcrsbkz', 'zkbsrchgry', 'wvyxchyfwhityvarcd', 'gf', 'zcna', 'vqdkdatklmbs', 'pepsfi', 'hknsjqnkfy', 'upkxypalctunir', 'vizynyhmjqpmde']))
# print(strong_string(['pies','mysz','kot','kogut','tok','seip','kot'])),l;,k l