import sqlite3

arrays = []
n = sqlite3.connect(input())
cursor = n.cursor()
resultat = cursor.execute("""SELECT DISTINCT title FROM genres WHERE id 
IN (SELECT genre FROM films WHERE year > 2009 AND year < 2012)""")
for f in resultat:
    if f[0] not in arrays:
        arrays.append(f[0])
for i in arrays:
    print(i)
n.close()
