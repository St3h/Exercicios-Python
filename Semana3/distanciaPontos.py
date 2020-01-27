import math

x1 = float(input('Insira o valor da abcissa x1: '))
y1 = float(input('Insira o valor da ordenada y1: '))
x2 = float(input('Insira o valor da abcissa x2: '))
y2 = float(input('Insira o valor da ordenada y2: '))

distance = math.sqrt( (x1 - x2)**2 + (y1 - y2)**2)

if distance >= 10:
    print('longe')
else:
    print('perto')