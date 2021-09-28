from random import shuffle, choice, randrange

m = input()
n = input()
s = int(input())
inqr = []
for i in m.split(", "):
    inqr.append(i)
c = []

for i in n:
    a = choice(inqr)
    c.append(a)

for i in n:
    x = randrange(s)
    symma = sum(x)
print()