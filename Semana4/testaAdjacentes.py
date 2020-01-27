num = int(input('Digite um número inteiro: '))
adjacent = False

while num > 0 and adjacent == False:
    digit = num % 10
    num = num // 10

    if num % 10 == digit:
        adjacent = True
    else:
        adjacent = False

if adjacent:
    print('sim')
else:
    print('não')
        





