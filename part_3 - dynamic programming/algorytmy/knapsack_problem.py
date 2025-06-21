def knapsack(W,P,B):
    n = len(W)
    F = [[0 for b in range(B+1)] for i in range(n)]
    for b in range(W[0], B+1):
        F[0][b] = P[0]
    for b in range(B+1):
        for i in range(n):
            F[i][b] = F[i-1][b]
            if b - W[i] >= 0:
                F[i][b] = max(F[i][b], F[i-1][b-W[i]] + P[i])
                
    return F[-1][-1]

knapsack(
    [3,1,3,4,2], # wagi
    [2,2,4,5,3], # wartości
    7
)
