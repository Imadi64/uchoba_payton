N = int(input())
text = [input() for _ in range(N)]
for t in text:
    if t[:4] == '####':
        continue

    if t[:2] == '%%':
        print(t[2:])
    else:
        print(t)
