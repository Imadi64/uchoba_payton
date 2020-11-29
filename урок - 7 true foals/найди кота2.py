strings = [input()]
i = 0
while strings[i] != 'СТОП':
    strings.append(input())
    i += 1

for item in range(len(strings)):
    if 'кот' in strings[item]:
        print(item + 1)
        break
else:
    print(-1)
