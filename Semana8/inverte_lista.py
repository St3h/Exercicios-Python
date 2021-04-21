i = int(input('Digite um número: '))
lista = []

while i > 0:
    lista.append(i)
    i = int(input('Digite um número: '))

for i in lista[::-1]:
    print(i)
    
