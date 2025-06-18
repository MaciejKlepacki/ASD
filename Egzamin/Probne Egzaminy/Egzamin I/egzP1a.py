from egzP1atesty import runtests 

def titanic( W, M, D ):

    # decoding
    s = ''
    for i in W:
        s += M[ord(i)-65][1]
    for d in range(len(D)):
        D[d] = M[D[d]][1]

    # crypting
    dp = [float('inf') for _ in range(len(s)+1)]
    dp[0] = 0
    for i in range(1, len(s)+1):
        for code in D:
            l = len(code)
            if i >= l and s[i-l:i] == code:
                dp[i] = min(dp[i], dp[i-l] + 1)

    return dp[-1]

runtests ( titanic, recursion=False )