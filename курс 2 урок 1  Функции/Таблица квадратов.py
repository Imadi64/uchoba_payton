def squared(a, b, k):
    for i in range(a, b + 1):
        x = i ** 2
        if (i % 10 == a % 10) and (i != a):
            print("")
        if x % k == 0:
            continue

        print(f"{x:<4} ", end='')
    print("")


squared(4, 33, 9)
squared(11, 99, 10)
