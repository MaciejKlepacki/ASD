# Maciej Klepacki 425795

# 1. Sortowanie wartości float z tablicy T rosnąco, za pomocą algorytmu merge_sort
# 2. Dodanie nowej tablicy differences, która oblicza przechowuje róznicę między palikami
# 3. Zliczanie liczby wartości, które są większe lub równe od szerokości traktora
# 4. Zwrócenie tej wartości
# 5. Złozoność czasowa: O(nlog(n))
# 6. Złozoność pamięciowa: O(n)

from kol1testy import runtests

def merge_sort(T):
    if len(T) <= 1:
        return T
    mid = len(T)//2
    left = merge_sort(T[:mid])
    right = merge_sort(T[mid:])
    return merge(left, right)

def merge(left, right):
    result = [None] * (len(left) + len(right))
    l = r = index = 0
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
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

def ogrodzenie(M, D, T):
  n = len(T)
  T = merge_sort(T)
  difference = [0]*(n-1)
  for i in range(n-1):
     difference[i] = T[i+1]-T[i]
  # difference = merge_sort(difference)
  counter = 0
  for i in difference:
      if i >= D: counter += 1
  return counter


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ogrodzenie, all_tests = True )