kol = int(input())
goroda = set()
for i in range(kol):
    goroda.add(input())
gorod = input()
if gorod in goroda:
    print("TRY ANOTHER")
else:
    print("OK")
