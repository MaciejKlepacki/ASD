from zad6testy import runtests

def parking(X,Y):
    INF = float('inf')

    # tworzę macierz z odległościami
    D = [[INF for _ in range(len(Y))] for _ in range(len(X))]
    for b in range(len(X)):
        for p in range(b, len(Y) - len(X) + b + 1):
            D[b][p] = abs(X[b]-Y[p])
    for b in range(1, len(X)):
        for p in range(1, len(Y)):
            D[b][p] += min(D[b-1][:p])
    return min(D[-1])


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )