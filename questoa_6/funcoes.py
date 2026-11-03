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