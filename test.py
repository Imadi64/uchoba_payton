import datetime as datetime
import math

dateBd = input().split('.')
bioD = input().split('.')
today = datetime.date.today()
dateBday = datetime.date(int(dateBd[2]), int(dateBd[1]), int(dateBd[0]))
bioDay = datetime.date(int(bioD[2]), int(bioD[1]), int(bioD[0]))

P = bioDay - dateBday
P = str(P)
p = P.split()
P = int(p[0])
T1 = 23
T2 = 28
T3 = 33

sinus1 = (2 * math.pi * P) / T1
B1 = math.sin(sinus1) * 100

sinus2 = (2 * math.pi * P) / T2
B2 = math.sin(sinus2) * 100

sinus3 = (2 * math.pi * P) / T3
B3 = math.sin(sinus3) * 100

print(round(B1, 2))
print(round(B2, 2))
print(round(B3, 2))
