ingredient_hold_mn = set()
ingredient_eat = set()
ingredient_hold = int(input())
for i in range(ingredient_hold):
    ingredient_hold_mn.add(input())
name_recept_N = int(input())
for i in range(name_recept_N):
    name_recept = input()
    ingredient_eat_M = int(input())
    flag = True
    for j in range(ingredient_eat_M):
        ingredient_eat.add(input())
    for i in ingredient_eat:
        if  i not in ingredient_hold_mn:
            flag = False
    if flag:
        print(name_recept)
    ingredient_eat = set()
