def posiciona_frota(frota):
    # cria um tabuleiro 10x10 só com água (0)
    grid = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        grid.append(linha)

    # percorre cada tipo de navio no dicionário
    for tipo in frota:
        # cada tipo tem uma lista de navios
        for navio in frota[tipo]:
            # cada navio é uma lista de posições [linha, coluna]
            for posicao in navio:
                linha = posicao[0]
                coluna = posicao[1]
                grid[linha][coluna] = 1  # marca o navio

    return grid