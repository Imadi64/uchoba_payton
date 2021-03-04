def prime(number):
    a = 0
    for i in range(1, number + 1):
        if number % i == 0:
            a += 1
    if a == 2:
        return "Простое число"
    else:
        return "Составное число"



print(prime(4))
print(prime(3))