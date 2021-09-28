import sys

data = list(map(str.strip, sys.stdin))
data = [s.strip() for s in data]
coment = list(filter(lambda word: word[0] == '#', data))
for e in coment:
    print(f'Line {data.index(e) + 1}: {e[1:].strip()}')