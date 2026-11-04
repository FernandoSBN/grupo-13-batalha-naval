def posiciona_frota(frota):
    
    grid = []
    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        grid.append(linha)
    for tipo in frota:
        for navio in frota[tipo]:
            for posicao in navio:
                grid[posicao[0]][posicao[1]] = 1

    return grid


def afundados(frota, tabuleiro):
    total = 0
    for tipo in frota:
        for navio in frota[tipo]:
            
            afundou = True
            for posicao in navio:
                if tabuleiro[posicao[0]][posicao[1]] != 'X':
                    afundou = False
            if afundou:
                total += 1
    return total


def define_posicoes(linha, coluna, orientacao, tamanho):
    
    posicoes = []
    for i in range(tamanho):
        if orientacao == 'vertical':
            posicoes.append([linha + i, coluna])
        else:  # horizontal
            posicoes.append([linha, coluna + i])
    return posicoes


def posicao_valida(frota, linha, coluna, orientacao, tamanho):
    novas = define_posicoes(linha, coluna, orientacao, tamanho)

    for posicao in novas:
        
        if posicao[0] < 0 or posicao[0] > 9 or posicao[1] < 0 or posicao[1] > 9:
            return False

        
        for tipo in frota:
            for navio in frota[tipo]:
                if posicao in navio:
                    return False

    return True


def preenche_frota(frota, nome_navio, linha, coluna, orientacao, tamanho):
    
    posicoes = define_posicoes(linha, coluna, orientacao, tamanho)
    if nome_navio not in frota:
        frota[nome_navio] = []
    frota[nome_navio].append(posicoes)
    return frota