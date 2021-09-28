n = int(input())
while not (1 <= n <= 100):
    n = int(input())
h = int(input())
while not (0 <= h <= 12):
    h = int(input())
m = int(input())
while not (0 <= m <= 59):
    m = int(input())
t = int(input())
while not (1 <= t <= 300):
    t = int(input())
x = (n * (h * 60 + m)) // t
print(x)