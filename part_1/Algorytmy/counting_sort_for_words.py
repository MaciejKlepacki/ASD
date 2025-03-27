def counting_sort_words(s):
    n = len(s)
    if n < 2:
        return s
    B = [None] * n
    C = [0] * 26
    res = ''

    for i in range(n):
        C[ord(s[i]) - ord('a')] += 1

    for i in range(1,26):
        C[i] += C[i-1]

    for i in range(n-1,-1,-1):
        B[C[ord(s[i]) - ord('a')] - 1] = s[i]
        C[ord(s[i]) - ord('a')] -= 1

    for letter in B:
        res += letter
    return res