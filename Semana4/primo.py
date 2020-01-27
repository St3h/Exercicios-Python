num = int(input('Digite um número inteiro: '))
prime = True 
divisor = 2

while divisor < num and prime == True:

    if num % divisor == 0:
        prime = False 
    else:
        divisor += 1

if prime:
    print('primo')
else:
    print('não primo')



