from egz1btesty import runtests
inf = float('inf')

def planets( D, C, T, E ):
    n = len(D)
    F = [[inf for f in range(E+1)] for i in range(n)]

    for f in range(E+1):
        F[0][f] = f * C[0]
    telep_to = T[0][0]
    telep_cost = T[0][1]
    F[telep_to][0] = telep_cost

    for i in range(1, n-1):
        c = C[i] # koszt benzyny na planecie i
        dist = D[i] - D[i-1] # dystans
        F[i][0] = min(F[i-1][dist], F[i][0])
        for f in range(1, E+1):
            prev = F[i-1][f+dist] if  f+dist <= E else inf
            F[i][f] = min(prev, F[i][f-1] + c)
        telep_to = T[i][0]
        telep_cost = T[i][1]
        F[telep_to][0] = min(F[telep_to][0], telep_cost + F[i][0])

    i = n-1
    dist = D[i] - D[i - 1]
    F[i][0] = min(F[i-1][dist], F[i][0])

    return F[n-1][0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
