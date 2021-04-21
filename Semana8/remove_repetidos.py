def remove_repetidos(x):
    lista = []
    for i in x:
        if i not in lista:
            lista.append(i)
    lista.sort()
    return lista 
