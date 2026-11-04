<<<<<<< HEAD
def posiciona_frota(frota):
    tabuleiro = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)
    for navio in frota:
        for posicao in frota[navio]:
            linha = posicao[0]
            coluna = posicao[1]
            tabuleiro[linha][coluna] = navio 
    return tabuleiro
=======
def define_posicoes(linha, coluna, orientacao, tamanho):
    posicoes = []
    if orientacao == 'horizontal':
        for i in range(tamanho):
            posicoes.append([linha, coluna + i])
    elif orientacao == 'vertical':
        for i in range(tamanho):
            posicoes.append([linha + i, coluna])
    return posicoes
>>>>>>> 29ef39ef28616550e951a2928389000914184898
