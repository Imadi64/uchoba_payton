print(" Ответте на несколько вопросов.")
print("Предусмотренно четыре варианта ответов\n\"да\", \"нет\", \"наверно\", \"незнаю\".")

print("Любите ли вы помогать?")
otvet = input()
if "нет" in otvet or "не " in otvet:
    t1 = "Вы неготовы помогать,"
elif "да" in otvet or "люблю" in otvet or "конечно" in otvet:
    t1 = "Вы готовы помочь,"
elif "наверно" in otvet:
    t1 = "Вы неуверены в себе,"
elif "незнаю" in otvet or "" == otvet:
    t1 = "Вы нехотите прилогать усилие,"
else:
    t1 = "Вы невнимательны"
    print("Предусмотренно четыре варианта ответов\n\"да\", \"нет\", \"наверно\", \"незнаю\".")

print("Помоглибы незнакомому человеку?")
otvet = input()
if "нет" in otvet or "не " in otvet:
    t2 = "и не хотите проявить заботу,"
elif "да" in otvet or "помог" in otvet or "конечно" in otvet:
    t2 = "и можете придти на помощь,"
elif "наверно" in otvet:
    t2 = "и сомниваетесь в своих намереньях,"
elif "незнаю" in otvet or "" == otvet:
    t2 = "и нехотите принимать важные решения,"
else:
    t2 = "вы невнимательны"
    print("Предусмотренно четыре варианта ответов\n\"да\", \"нет\", \"наверно\", \"незнаю\".")

print("Вы готовы нести ответственность за ошибки?")
otvet = input()
if "нет" in otvet or "не" in otvet:
    t3 = "а такж не готовы брать на себя ответственность,"
elif "да" in otvet or "готов" in otvet or "конечно" in otvet:
    t3 = "а так же готовы проявить ответственность,"
elif "наверно" in otvet:
    t3 = "а так же можете взять на себя ответственность,"
elif "незнаю" in otvet or "" == otvet:
    t3 = "а так же не можете отвечать за поступки,"
else:
    t3 = "вы невнимательны"
    print("Предусмотренно четыре варианта ответов\n\"да\", \"нет\", \"наверно\", \"незнаю\".")

print("Готовы много работать?")
otvet = input()
if "нет" in otvet or "не " in otvet:
    t4 = "не готовы много работать,"
elif "да" in otvet or "готов" in otvet or "конечно" in otvet:
    t4 = "готовы много работать,"
elif "наверно" in otvet:
    t4 = "способны работать,"
elif "незнаю" in otvet or "" == otvet:
    t4 = "не сможете работать,"
else:
    t4 = "вы невнимательны"
    print("Предусмотренно четыре варианта ответов\n\"да\", \"нет\", \"наверно\", \"незнаю\".")

print("Вы готовы терпеть плохой коллектив?")
otvet = input()
if "нет" in otvet or "не " in otvet:
    t5 = "при всем этом не можете терпеть причуды друзей."
elif "да" in otvet or "готов" in otvet or "конечно" in otvet:
    t5 = "при всём этом способны сохронять спакойствие в стрессовых ситуациях."
elif "наверно" in otvet:
    t5 = "при всем этом можете некоторые вредности стерпеть."
elif "незнаю" in otvet or "" == otvet:
    t5 = "при всем этом не знаете как вести себя в коллективе."
else:
    t5 = "вы невнимательны"
    print("Предусмотренно четыре варианта ответов\n\"да\", \"нет\", \"наверно\", \"незнаю\".")

print(t1, t2, t3, t4, t5)
