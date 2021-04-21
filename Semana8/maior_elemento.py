def maior_elemento(x):
    maior = x[0]
    for i in x:
        if i > maior:
            maior = i
    return maior 