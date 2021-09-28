def roots_of_quadratic_equation(a, b, c):
    result = []
    if a == 0 and b == 0 and c == 0:
        result.append("all")
        return result
    elif a == 0 and b == 0:
        return []
    elif a == 0:
        result.append(-c / b)
    else:
        d = b ** 2 - 4 * a * c
        if d > 0:
            result.append((-b + d ** 0.5) / (2 * a))
            result.append((-b - d ** 0.5) / (2 * a))
        elif d == 0:
            result.append(-b / (2 * a))
        else:
            return []
        return result




result = roots_of_quadratic_equation(1, 2, 1)
print(*sorted(result))
result = roots_of_quadratic_equation(1, -3, 2)
print(*sorted(result))