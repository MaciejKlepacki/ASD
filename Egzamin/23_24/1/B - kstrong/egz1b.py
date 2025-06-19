from egz1btesty import runtests


def kstrong(T, k):

    n = len(T)
    F = [[0 for _ in range(k+1)] for _ in range(n)]

    F[0][0] = T[0]

    for i in range(1,n):
        F[i][0] = max(T[i], T[i] + F[i-1][0])

    result = 0
    for nk in range(1, k+1):
        for i in range(1, n):
            F[i][nk] = max(T[i] + F[i-1][nk], F[i-1][nk-1])
            result = max(result, F[i][nk])

    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(kstrong, all_tests=True)