l = int(input('digite a largura: '))
h = int(input('digite a altura: '))

linha = 1
coluna = 1

while linha <= h:
    while coluna <= l:
        print('#', end = '')
        coluna += 1
    linha += 1
    print()
    coluna = 1
    
    