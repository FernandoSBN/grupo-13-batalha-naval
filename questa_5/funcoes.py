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