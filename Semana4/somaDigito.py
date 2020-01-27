interge = int(input('Digite um número inteiro: '))
divisor = 10
num = interge
amount = 0

while num > 0:
    digit = num % divisor
    amount += digit
    num = num // divisor
print(amount)



    
