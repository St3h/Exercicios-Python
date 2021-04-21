def éPrimo(k):
    divisor = 1
    count = 0
    while divisor <= k:
        if k % divisor == 0:
            count += 1
        divisor += 1

    if count > 2:
        return False
    else:
        return True 

def n_primos(n):
    count = 0
    while n >= 2:
        if éPrimo(n) == True:
            count += 1
            n -= 1
        else:
            n -= 1
    return count

    
    
