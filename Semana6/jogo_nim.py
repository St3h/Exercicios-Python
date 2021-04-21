def computador_escolhe_jogada(n, m):

    movimento = 1

    while movimento != m:

        if (n - movimento) % (m + 1) == 0:
            return movimento
        else:
            movimento += 1
            

    return movimento

def usuario_escolhe_jogada(n, m):

    movimento = int(input('Quantas peças você vai tirar?'))

    if movimento > m or movimento < 1:
        print('Oops! Jogada inválida! Tente de novo.')
    else:
        return movimento

def partida():
    
    n = int(input('Quantas peças?'))
    m = int(input('Limite de peças por jogada?'))

    computador_jogada = True

    #escolha da primeira jogada
    if n % (m + 1) == 0:
        print('Voce começa!')
        computador_jogada = False 
    else:
        print('Computador começa!')
        computador_jogada = True 
    
    #jogadas
    while n > 0:

        if computador_jogada == True:
            movimento = computador_escolhe_jogada(n, m)
            n -= movimento
            
            if movimento == 1:
                print('O computador tirou uma peça.')
            else:
                print('O computador tirou',movimento,'peças.')
            
            computador_jogada = False

        else:
            movimento = usuario_escolhe_jogada(n, m)
            n -= movimento

            if movimento == 1:
                print('O computador voce uma peça.')
            else:
                print('Voce tirou',movimento,'peças.')
            
            computador_jogada = True
        
        if n == 1:
            print('Agora resta apenas uma peça no tabuleiro.')
        if n > 1:
            print('Agora restam,',n, 'peças no tabuleiro.')

    if computador_jogada:
        print('Fim de jogo! Você ganhou')
    else:
        print('Fim de jogo! O computador ganhou')

def campeonato():

    rodada = 1

    while rodada <= 3:
        print('**** Rodada',rodada,'****')
        print()
        partida()
        rodada += 1
    print('Placar: Você 0 X 3 Computador')

    
print('Bem-vindo ao jogo do NIM! Escolha:') 
print()

print('1 - para jogar uma partida isolada')

modalidade = int(input('2 - para jogar um campeonato'))

if modalidade == 1:
    print()
    print('Voce escolheu jogar uma partida!')
    partida()

if modalidade == 2:
    print()
    print('Voce escolheu um campeonato!')
    campeonato()