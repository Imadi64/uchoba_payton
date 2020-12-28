s = []
for i in range(30001):
    s.append(0)
pos = 0
a = list(input())
for i in range(len(a)):
    if a[i] == ">":
        pos = pos + 1
    elif a[i] == "<":
        pos = pos - 1
    elif a[i] == ".":
        print(s[pos])
    elif a[i] == "+":
        s[pos] = s[pos] + 1
    elif a[i] == "-":
        s[pos] = s[pos] - 1
    elif a[i] == '[':
        if s[pos] == 0:
            while a[i] != ']':
                i += 1
    if s[pos] > 255:
        s[pos] = 0
    elif s[pos] < 0:
        s[pos] = 255







english_n = int(input())
german_n = int(input())
languages = set()
surnames = set()
for i in range(english_n + german_n):
    surname = input()
    if surname in languages:
        surnames.add(surname)
    else:
        languages.add(surname)
difference = languages - surnames
if not difference:
    print('NO')
else:
    print(len(difference))