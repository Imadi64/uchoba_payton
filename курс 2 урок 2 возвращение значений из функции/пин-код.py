def IsPrime(n):
    m = 2
    while m * m <= n and n % m != 0:
        m += 1
    return m * m > n and n > 1


def is_palindrom(string):
    return str(string) == str(string)[::-1]


def is_2_pow(n):
    return bin(n).count('1') == 1


def check_pin(pinCode):
    x = [int(i) for i in pinCode.split('-')]
    return 'Корректен' if (IsPrime(x[0]) and is_palindrom(x[1]) and is_2_pow(x[2])) else 'Некорректен'


print(check_pin('1-101-32'))
print(check_pin('7-101-4'))
print(check_pin('12-22-16'))