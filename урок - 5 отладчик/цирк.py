a = int(input())
shag = 0
while a != 1:
    if a % 2 == 0:
        a /= 2
    else:
        a -= 1
    shag += 1
print(shag)