n = int(input())
familii = []
for i in range(n):
    familii.append(input())
f = 0
for i in familii:
    if familii.count(i) == 1:
        f += 1
print(n - f)
