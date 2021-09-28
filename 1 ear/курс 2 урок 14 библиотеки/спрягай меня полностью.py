import pymorphy2

morph = pymorphy2.MorphAnalyzer()

a = input()
word = morph.parse(a)[0]
if 'VERB' in word.tag.POS:
    print('Прошедшее время:')
    print(word.masc.past)
    print(word.femn.past)
    print(word.neut.past)
    print(word.plur.past)
    print('Настоящее время:')
    
