def catalan(n):
    if n == 0:
        return 1
    return catalan(n - 1) * 2 * (2 * n - 1) // (n + 1)




print(catalan(0))
print(catalan(1))
print(catalan(45))