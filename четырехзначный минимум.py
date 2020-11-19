chislo = int(input())
a = chislo % 10
chislo //= 10
b = chislo % 10
chislo //= 10
c = chislo % 10
d = chislo // 10
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if c > d:
    c, d = d, c
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
if a == 0 and b:
    a, b = b, a
elif a == 0 and c:
    a, c = c, a
elif a == 0 and d:
    a, d = d, a
print(d + 10 * (c + 10 * (b + 10 * a)))


# chislo = input()
# a = int(chislo[0])
# b = int(chislo[1])
# c = int(chislo[2])
# d = int(chislo[3])
# if a > b:
#     a, b = b, a
# if b > c:
#     b, c = c, b
# if c > d:
#     c, d = d, c
# if a > b:
#     a, b = b, a
# if b > c:
#     b, c = c, b
# if a > b:
#     a, b = b, a
# if a == 0 and b:
#     a, b = b, a
# elif a == 0 and c:
#     a, c = c, a
# elif a == 0 and d:
#     a, d = d, a
# print(d + 10 * (c + 10 * (b + 10 * a)))


# chislo = int(input())
# a = chislo % 10
# chislo //= 10
# b = chislo % 10
# chislo //= 10
# c = chislo % 10
# d = chislo // 10
# a, b, c, d = sorted((a, b, c, d))
# if a == 0 and b:
#     a, b = b, a
# elif a == 0 and c:
#     a, c = c, a
# elif a == 0 and d:
#     a, d = d, a
# print(a*10**3 + b*10**2 + c*10**1 + d*10**0)


# chislo = input()
# a = "".join(sorted(chislo))
# print(a)