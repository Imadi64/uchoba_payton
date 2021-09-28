def cached(m):
    def fib(n):
        if n == 1 or n == 2:
            rezalt = 1
        else:
            rezalt = fib(n - 1) + fib(n - 2)
        return rezalt


rezyltat =  cached(1)
print(rezyltat)


@cached
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)