from zad7testy import runtests


# def orchard(T, m):
#     n = len(T)
#     F = [[n] * m for _ in range(n)]
#
#     F[0][0] = 1  # zawsze mogę usunąć pierwsze drzewo
#     F[0][T[0] % m] = 0  # warunek brzegowy - nie wycinam drzew aby otrzymać resztę z 0-drzewa
#
#     for i in range(1, n):
#         for j in range(m):
#             F[i][j] = min(F[i][j], F[i - 1][j] + 1)  # mogę ściąć drzewo
#
#             future_rest = (j + T[i]) % m
#             F[i][future_rest] = min(F[i][future_rest], F[i - 1][j])
#     print(F)
#     return F[n - 1][0]

# def orchard(T, m):
#     S = sum(T)
#     r = S % m
#     if r == 0:
#         return 0  # nic nie trzeba usuwać
#
#     n = len(T)
#     # dp[i] = najmniejsza liczba elementów, których suma % m == i
#     dp = [float('inf')] * m
#     dp[0] = 0  # suma 0 osiągamy bez żadnych elementów
#
#     for t in T:
#         ndp = dp[:]
#         for mod in range(m):
#             new_mod = (mod + t) % m
#             if dp[mod] + 1 < ndp[new_mod]:
#                 ndp[new_mod] = dp[mod] + 1
#         dp = ndp
#
#     return dp[r] if dp[r] != float('inf') else -1  # jeśli nie da się, zwracamy -1

# def orchard(T, m):
#     n = len(T)
#
#     # skracam tablice T
#     t = 0
#     while t < n:
#         if T[t] % m == 0:
#             T.pop(t)
#             n -= 1
#         else:
#             t += 1
#     print(T)
#
#     F = [[float('inf') for mod in range(m)] for i in range(n)]
#     F[0][0] = 1
#     F[0][T[0]%m] = 0
#
#     for mod in range(m):
#         for i in range(1, n):
#             F[i][mod] = min(F[i-1][mod], )

def orchard(T, m):
    n = len(T)
    INF = float('inf')

    # F[i][j][r] = czy da się wybrać j elementów spośród pierwszych i, dających resztę r
    F = [[[INF] * m for _ in range(n+1)] for _ in range(n+1)]

    F[0][0][0] = 0  # 0 elementów, suma 0 => 0 usunięć

    for i in range(1, n+1):
        for j in range(i+1):  # nie możesz zachować więcej niż i elementów
            for r in range(m):
                # przypadek: nie biorę i-tego elementu
                if F[i-1][j][r] != INF:
                    F[i][j][r] = min(F[i][j][r], F[i-1][j][r] + 1)

                # przypadek: biorę i-ty element
                if j > 0:
                    prev_r = (r - T[i-1]) % m
                    if F[i-1][j-1][prev_r] != INF:
                        F[i][j][r] = min(F[i][j][r], F[i-1][j-1][prev_r])

    # Szukamy minimum liczby usunięć (czyli n - j), gdy suma % m == 0
    result = INF
    for j in range(n+1):
        if F[n][j][0] != INF:
            result = min(result, F[n][j][0])

    return result if result != INF else -1
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True   )
# orchard([2,2,7,5,1,14,7], 7)