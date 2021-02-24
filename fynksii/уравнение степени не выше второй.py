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



print(sorted(solve(1, 2, 1)))
