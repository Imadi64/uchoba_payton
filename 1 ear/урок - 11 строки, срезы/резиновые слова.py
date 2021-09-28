сlovo = input()
n = len(сlovo)
z = (n - 1) // 2
c = ' ' * z + сlovo[z: z + (n - 1) % 2 + 1]
print(c)
for i in range(1, z + 1):
    t = (z - i) * ' ' + сlovo[z - i] + ' ' * (2 * i - n % 2) + сlovo[z + i + (n - 1) % 2]
    print(t)
