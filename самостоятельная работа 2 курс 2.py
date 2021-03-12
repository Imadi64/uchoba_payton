import random
"""модуль datatame
import datetime

a = datetime.datetime.today().strftime("%Y%m%d")
print(a) # '20170405'

today = datetime.datetime.today()
print( today.strftime("%m/%d/%Y") ) # '04/05/2017'

print( today.strftime("%Y-%m-%d-%H.%M.%S") ) # 2017-04-05-00.18.00

РАЗНИЦА МЕЖДУ ДВУМЯ ДАТАМИ
import datetime

# Значение: datetime.datetime(2017, 4, 5, 0, 18, 51, 980187)
now = datetime.datetime.now()

then = datetime.datetime(2017, 2, 26)

# Кол-во времени между датами.
delta = now - then

print(delta.days) # 38
print(delta.seconds) # 1131


"""

''' модуль рандом
from random import randrange, randint

# возвращаем случайное целое из диапазона
print(randrange(100))
print(randrange(40, 100, 5))
print(randint(10, 20))

моделирование подкидывания монетки:
from random import choice
choice((1, 2))

имитация подбрасывания 2-х кубиков(цифры)
from random import choice

dashes = [1, 2, 3, 4, 5, 6]
for i in range(1, 10):
    print(choice(dashes), choice(dashes))


from random import choice(кубики)

dashes = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
for i in range(1, 10):
    print(choice(dashes), choice(dashes))
    
import random
 
 
print("Использование random.randint() для генерации случайного целого числа")
print(random.randint(0, 5))
print(random.randint(0, 5))

'''
help(random)