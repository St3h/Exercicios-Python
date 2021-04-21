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

def maior_primo(n):
    while éPrimo(n) == False:
        n -= 1
    return n 


























