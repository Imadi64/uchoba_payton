mir = 'Остазия'
voina = 'Евразия'
n = int(input())
for i in range(n):
    komanda = input()
    if komanda == 'С кем война?':
        print(voina)
    if komanda == 'С кем мир?':
        print(mir)
    if komanda == "Меняем":
        voina, mir = mir, voina
