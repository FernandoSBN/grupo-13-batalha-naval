def posiciona_frota(frota):
    tabuleiro = [[0 for coluna in range(10)] for linha in range(10)]

    for navio in frota:
        for coordenada in frota[navio]:
            linha = coordenada[0]
            coluna = coordenada[1]

            tabuleiro[linha][coluna] = 1

    return tabuleiro