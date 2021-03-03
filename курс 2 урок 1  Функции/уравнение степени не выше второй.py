

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
