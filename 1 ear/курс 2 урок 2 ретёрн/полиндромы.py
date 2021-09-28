def palindrome(s):
    s = s.replace(' ', '').lower()
    if s == s[::-1]:
        return "Палиндром"
    else:
        return "Не палиндром"




print(palindrome('А роза упала на лапу Азора'))
print(palindrome('Палиндром'))