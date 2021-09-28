import pymorphy2
import sys

morph = pymorphy2.MorphAnalyzer()
text = sys.stdin.read().split()
live = morph.parse('живой')[0]
for i in text:
    i = morph.parse(i)[0]
    if 'NOUN' not in i.tag:
        print('Не существительное')
    elif i.tag.animacy == 'inan':
        print('Не ' + live.inflect({str(i.tag.number), str(i.tag.gender)})[0])
    else:
        live = morph.parse('живой')[0]
        print(live.inflect({str(i.tag.number), str(i.tag.gender)})[0].capitalize())
