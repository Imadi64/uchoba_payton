max_d = 0
number = 0
a = int(input())
for i in range(a):
    n = int(input())
    min_t = 1000000
    for j in range(n):
        h = int(input())
        if h < min_t:
            min_t = h
    if min_t > max_d:
        max_d = min_t
        number = i + 1
print(number, max_d)
