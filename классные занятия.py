class TooLargeError(Exception):
    pass


def boats(*a):
    h = 0
     = []
    for i in a:
        if i % 21 != 0:
            nysh_lodki.append(i)
        if not (isinstance(i, int)):
            raise TypeError('Incorrect argument')
        elif  >= 1000000:
            raise TooLargeError('All values cannot be so large')
        elif len(nysh_lodki) == 0:
            raise ZeroDivisionError('No matching numbers')


    for i in nysh_lodki:
        h += i
        t = h / len(nysh_lodki)
    return round(t, 2)


data = [168, 42, 198, 63, 152, 3, 14]
print(boats(*data))
