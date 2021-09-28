small_symbols = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
big_symbols = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def shift(text, symbols, n):
    index = symbols.find(text)
    if index + n < len(symbols):
        return symbols[index + n]
    else:
        return symbols[(index + n) % len(symbols)]


def back_shift(text, symbols, n):
    index = symbols.find(text)
    if index - n >= 0:
        return symbols[index - n]
    else:
        return symbols[(index - n) % len(symbols)]


def encrypt(text, n=3, i=0, res=""):
    if (len(res) == len(text)): return res

    if text[i].isupper():
        res += shift(text[i], big_symbols, n)

    elif text[i].islower():
        res += shift(text[i], small_symbols, n)
    else:
        res += text[i]

    return encrypt(text, n, i + 1, res)


def decrypt(text, n=3, i=0, res=""):
    if (len(res) == len(text)): return res

    if text[i].isupper():
        res += back_shift(text[i], big_symbols, n)

    elif text[i].islower():
        res += back_shift(text[i], small_symbols, n)
    else:
        res += text[i]

    return decrypt(text, n, i + 1, res)


str = encrypt(input())
print(str)
print(decrypt(str))
