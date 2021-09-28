def eratosthenes(N):
    a = [n for n in range(N + 1)]
    a[0] = 0
    a[1] = 0
    for i in range(2, len(a)):
        if a[i] > 0:
            for j in range(i * i, N + 1, i):
                if a[j] > 0:
                    print(a[j], end=" ")
                    a[j] = 0
    a = [x for x in a if x > 0]
    print(str(a))


eratosthenes(15)