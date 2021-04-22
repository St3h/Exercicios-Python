'''DETECTOR DE AUTORIA'''
'''Este programa compara traços linguisticos entres diferntes textos que recebe para identificar a autoria dos mesmos'''

import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma ass_a a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
                del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
             freq[p] = 1
             unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def calcula_assinatura(texto):

    ass_a = []

# tamanho médio das palavras
    lista_sentencas_texto = separa_sentencas(texto)

    lista_frases_texto = []
    for i in lista_sentencas_texto:
        frases = separa_frases(i)
        for i in frases:
            lista_frases_texto.append(i)
    
    lista_palavras = []
    for i in lista_frases_texto:
        palavras_separadas = separa_palavras(i)
        for i in palavras_separadas:
            lista_palavras.append(i)

    somaPalavras = len(lista_palavras)

    somaTamanho = 0
    for i in lista_palavras:
        tamanho = len(i)
        somaTamanho += tamanho
    wal = somaTamanho / somaPalavras
    ass_a.append(wal)
    
# type-token

    palavras_diferentes = n_palavras_diferentes(lista_palavras)
    ttr = palavras_diferentes / somaPalavras
    ass_a.append(ttr)

# razão hapax

    palavras_unicas = n_palavras_unicas(lista_palavras)
    hlr = palavras_unicas / somaPalavras
    ass_a.append(hlr)

# tamanho médio das sentenças 

    lista_sentencas = separa_sentencas(texto)
    somaSentencas = len(lista_sentencas)
    
    somaTamanhoSentenca = 0
    for i in lista_sentencas:
        caracteres = len(i)
        somaTamanhoSentenca += caracteres
    sal = somaTamanhoSentenca / somaSentencas
    ass_a.append(sal)
    
# Complexidade da sentença 

    lista_frases = []
    for i in lista_sentencas:
        frases = separa_frases(i)
        for i in frases:
            lista_frases.append(i)
    
    somaFrases = len(lista_frases)
    sac = somaFrases / somaSentencas
    ass_a.append(sac)

# Tamanho médio da frase 

    somaTamanhoFrase = 0
    for i in lista_frases:
        letras = len(i)
        somaTamanhoFrase += letras
    pal = somaTamanhoFrase / somaFrases
    ass_a.append(pal)

    return  ass_a
    
def avalia_textos(textos, ass_cp):
    
    i = len(textos) -1
    tex = 0
    lista = []
    while tex <= i:
        a = calcula_assinatura(textos[tex])
        lista.append(compara_assinatura(a,ass_cp))
        tex += 1
    
    tex = 1
    for item in lista:
        if item == min(lista):
            return tex
        else:
            tex +=1  

def compara_assinatura(as_a, as_b):
    
    soma_a = 0
    soma_b = 0
    for i in as_a:
        soma_a = soma_a+i
    for i in as_b:
        soma_b = soma_b+i
   
    if soma_a >= soma_b:     
        ass = (soma_a - soma_b)/6
    else:
        ass= (soma_b - soma_a)/6
        
    return ass
