l = int(input('digite a largura: '))
h = int(input('digite a altura: '))

linha = 1
coluna = 1

while linha <= h:
    while coluna <= l:
        if (linha == 1 or linha == h) or (coluna == 1 or coluna == l):
            print('#', end = '')
            coluna += 1
        else:
            print(' ', end = '')
            coluna += 1
    linha += 1
    print()
    coluna = 1