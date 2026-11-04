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
                linha = posicao[0]
                coluna = posicao[1]
                grid[linha][coluna] = 1  

    return grid