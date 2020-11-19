voprosi = ("Привет. Как дела?", "Как работа?",
           "Как здоровье?", "Как дети?",
           "Нравится ли тебе коты?", "Как успеваемость?")
otveti_bota_pol = ("Прекрасно, и у меня.", "Хорошо когда работа хорошая.",
                   "Я рад, что все хорошо.", "Я рад, что дети впорядке.",
                   "Мне они тоже нравятся.", "Молодец.")
otveti_bota_otr = ("Жаль, но в скоре все наладится.", "Работа должна приносить радость. Отдохни.",
                   "Выздоравливай и закаляйся.", "Подрастут, будет легче.",
                   "А мне нравятся.", "Старайся.")
otveti_bota_neopr = ("Пусть так.", "Не понял.",
                     "Больше отдыхай.", "Понятно.",
                     "Впринцыпе, животина это прикольно", "Понял")
pol = ("хорошо", "прекрасно", "отлично", "замечательно", "нормально", "нравится", "класно", "да")
otr = ("плохо", "ужасно", "отвратительно", "ненравится", "скучно", "неочень", "нет")
neopr = ("?", "не")
i = 0
while i < len(voprosi):
    vopros = voprosi[i]
    otvet_pol = otveti_bota_pol[i]
    otvet_otr = otveti_bota_otr[i]
    otvet_neopr = otveti_bota_neopr[i]
    i += 1
    print(vopros)
    otvet_polzov = str.lower(input())
    if set(neopr) & set(otvet_polzov.split()):
        print(otvet_neopr)
    elif set(pol) & set(otvet_polzov.split()):
        print(otvet_pol)
    elif set(otr) & set(otvet_polzov.split()):
        print(otvet_otr)
    else:
        print(otvet_neopr)
