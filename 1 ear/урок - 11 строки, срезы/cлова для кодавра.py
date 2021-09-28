vow = 'аеёиоуыэюя'
cons = 'бвгджзйклмнпрстфхцчшщьъ'
p1 = input()
res = []
for w in iter(input, ''):
    p = p1
    k = 0
    if '*' in p and len(w) + 2 > len(p):
        p = p.replace('*', '?' * (len(w) - len(p) + 1))
    if len(w) == len(p):
        n = len(w)
        for i in range(n):
            if (p[i] == '?' or (w[i] in vow and p[i] == '0')
                    or (w[i] in cons and p[i] == '1')):
                k = 1
            else:
                k = 0
                break
    if k:
        res.append(w)
if res:
    print(*res, sep='\n')
else:
    print('Есть нечего, значить!')
