def squared(a, b, k):
    for i in range(a, b + 1):
        if i % k == 0:
            print("")
        else:
            print(i * i, end='\t')


squared(4, 33, 9)
