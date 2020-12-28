menu = set()
ispol_menu = set()
ne_ispol_menu = set()
menu_N = int(input())
for i in range(menu_N):
    menu.add(input())
menu_na_segodna = int(input())
for i in range(menu_na_segodna):
    menu_in_day_N = int(input())
    for j in range(menu_in_day_N):
        ispol_menu.add(input())
ne_ispol_menu = menu - ispol_menu
for i in ne_ispol_menu:
    print(i)
