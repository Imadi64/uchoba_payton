kon_gor = float(input())
kon_1 = float(input())
kon_2 = float(input())
t_noch = int(input())
ispor_d = float(input())
if t_noch * kon_gor >= ispor_d:
    kon_gor = "Конек-Горбунок"
else:
    kon_gor = ""
if t_noch * kon_1 >= ispor_d:
    kon_1 = "Лошадиного брата - 1"
else:
    kon_1 = ""
if t_noch * kon_2 >= ispor_d:
    kon_2 = "Лошадиный брат - 2"
else:
    kon_2 = ""
if kon_gor == "" and kon_1 == "" and kon_2 == "":
    print("Не они!")
else:
    print(kon_gor, kon_1, kon_2)