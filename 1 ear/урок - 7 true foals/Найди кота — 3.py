# strochka = input()
# str_k = 0
# koshak = 0
# n = 0
# while strochka != 'СТОП':
#     if n == 0:
#         str_k += 1
#
#     if ("Кот" in strochka) or ("кот" in strochka):
#         koshak += 1
#         n = 1
#     strochka = input()
# print(koshak, n)

strochka = input()
str_k = 0
koshak = 0
while strochka != 'СТОП':
    if koshak == 0:
        str_k += 1
    if ("Кот" in strochka) or ("кот" in strochka):
        koshak += 1
    strochka = input()
if koshak == 0:
    str_k = -1
print(koshak, str_k)
