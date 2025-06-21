# Maciej Klepacki

# n, i - wysokość / height
# m, j - szerokość / width

# Złozoność: O(nm)

# Zaczynam 'rozszerzać' blat zaczynając od ostatniego bloku B[-1][-1], dokładając z kazdym ruchrm deski do lewej i do góry. 
# W przypadku, gdy wartość w tablicy F moze być mniejsza, aktualizuje ją
# W trakcie sprawdzam odpowiednie warunki, czy nie wyjdę w danym kroku za tablicę, oraz sprawdzam, czy suma sęk nie przekroczy liczby s
# Algorytm jest dynamiczny

from kol3testy import runtests

inf = float('inf')

def parkiet(B, C, s):
    n = len(B)
    m = len(B[0])
    F = [[inf for _ in range(m+1)] for _ in range(n+1)] # tablica do przechowywania liczby cięć dla danego kwaratu

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            cur_hight = n - i
            cur_width = m - j
            sum = C[i][j]

            if (cur_hight == 1 or cur_width == 1) and sum - s <= 0:
                F[i][j] = 0
                continue

            # height
            h = 0
            if i+1 < n:
                h = C[i+1][j]
            sum_row = sum - h
            if sum_row - s <= 0:
                F[i][j] = min(F[i][j], F[i+1][j] + 1)

            # width
            w = 0
            if j+1 < m:
                w = C[i][j+1]
            sum_column = sum - w
            if sum_column - s <= 0:
                F[i][j] = min(F[i][j], F[i][j+1] + 1)
    
    if F[0][0] < inf:
        return F[0][0]
    else:
        return -1

runtests(parkiet, all_tests = True)
