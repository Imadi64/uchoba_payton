lower_cyrillic = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н',
        'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы',
        'ь', 'э', 'ю', 'я']
upper_cyrillic = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н',
        'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы',
        'Ь', 'Э', 'Ю', 'Я']


def encrypt_caesar(shift):
    return lower_cyrillic[shift:] + \
           lower_cyrillic[:shift] + \
           upper_cyrillic[shift:] + \
           upper_cyrillic[:shift]


def decrypt_caesar(typ="enc", shift=3):
    a1 = lower_cyrillic + upper_cyrillic
    a2 = encrypt_caesar(shift)

    t = {
        "enc": str.maketrans(a1, a2),
        "dec": str.maketrans(a2, a1)
    }

    return t[typ]



msg = "Да здравствует салат Цезарь!"
shift = 5
encrypted = encrypt_caesar(msg, shift)
decrypted = decrypt_caesar(encrypted, shift)
print(encrypted)
print(decrypted)