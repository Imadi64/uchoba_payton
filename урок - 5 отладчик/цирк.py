a = int(input())
summ = 1
summ = summ + 1
h = 1
while summ != a:
    if summ * 2 < a:
        summ *= 2
    if summ * 2 > a:
        summ += 1
    h += 1
print(h)
