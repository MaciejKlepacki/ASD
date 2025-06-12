from zad9testy import runtests

inf = float('inf')

def joining_sorting(O, C, L):
    for i in range(len(O)):
        O[i] = (O[i], C[i])
    O.append((0, 0))
    O.append((L, 0))

    return O.sort()


def min_cost( O, C, T, L ):
    F = joining_sorting(O, C, L)
    n = len(O)
    dp1 = [float("inf") for _ in range(n)]
    dp2 = [float("inf") for _ in range(n)]
    dp1[0], dp2[0] = 0, 0

    for i in range(n):
        for j in range(i + 1, n):
            distance = O[j][0] - O[i][0]
            if distance <= T:
                dp1[j] = min(dp1[j], dp1[i] + O[i][1])
                dp2[j] = min(dp2[j], dp2[i] + O[i][1])
            elif distance <= 2 * T:
                dp2[j] = min(dp2[j], dp1[i] + O[i][1])

    return min(dp1[n - 1], dp2[n - 1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( min_cost, all_tests = True )