import pymorphy2

morth = pymorphy2.MorphAnalyzer()
res = morth.parse(input().split())
word = res[1]
if res.tag.POS[0] == "VERB":
    if res.tag.POS[1] == "NOUN":
        if res.inflect({'accs'} == word:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
else:
    print("NO")
