chislo = int(input())
ycheniki = []
otlichniki = []
for i in range(chislo):
    ycheniki.append(input())

for osenka in ycheniki:
    if osenka[-1] >= "4":
        otlichniki.append(osenka)

for ychen in ycheniki:
    print(ychen)

print()
for ychen in otlichniki:
    print(ychen)
