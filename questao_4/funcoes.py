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