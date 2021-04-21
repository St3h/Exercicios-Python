def éHipotenusa(k):
    i = 1
    j = 1

    while i < k:
        while j < k:
            if k**2 == i**2 + j**2:
                return True
            else:
                j += 1
        i += 1
        j = 1
    return False 


def soma_hipotenusas(n):
    soma = 0
    while n >= 1:
        if éHipotenusa(n) == True:
            soma += n
            n -= 1
        else:
            n -= 1
    return soma 
    
    
