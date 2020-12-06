d = int(input())
m = int(input())
g = int(input())
if m == 1 or m == 2:
    m += 10
else:
    m -= 2
y = g % 100
c = g // 100
w = d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)
den_ned = w % 7
print(den_ned)
