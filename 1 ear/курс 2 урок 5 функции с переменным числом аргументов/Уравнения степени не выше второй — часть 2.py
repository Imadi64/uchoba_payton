def roots_of_quadratic_equation(a, b, c: int):
    d = b ** 2 - 4 * a * c
    if d >= 0:
        x1 = (-b + d ** 0.5) / (2 * a)  # первый корень
        x2 = (-b - d ** 0.5) / (2 * a)
        x.append(x1)
        if x1 == x2:
            return x
        else:
            x.append(x2)
            return x
    else:
        return x


x = []


def solve(*coefficients: int):
    global x
    if len(coefficients) == 3:
        a, b, c = coefficients[0], coefficients[1], coefficients[2]
        return roots_of_quadratic_equation(a, b, c)
    elif len(coefficients) == 2:
        b, c = coefficients[0], coefficients[1]
        x.append(-c / b)
        return x
    elif len(coefficients) == 1:
        if coefficients[0] == 0:
            return ['all']
        else:
            return x
    else:
        return None
