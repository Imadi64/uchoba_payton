def roots_of_quadratic_equation(*k):
    a, b, c = k[0], k[1], k[2]
    D = b ** 2 - 4 * a * c  # дискриминант

    x1 = (-b + D ** 0.5) / (2 * a)  # первый корень
    x2 = (-b - D ** 0.5) / (2 * a)  # второй корень

    return x1, x2


def solve(*coeffs):
    if len(coeffs) == 3:
        return roots_of_quadratic_equation(*coeffs)
    elif len(coeffs) == 2:
        b, c = coeffs[0], coeffs[1]
        return -c / b
    else:
        return 0


def password(func):
    def check(n):
        k = input()
        if k != 'qwerty':
            print('В доступе отказано')
            return
        func(n)

    return check


@password
def fib(n):
    if n == 1 or n == 2:
        print(1)
    else:
        print(fib(n - 1) + fib(n - 2))
    return
