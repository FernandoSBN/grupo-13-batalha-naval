def define_posicoes(linha,coluna,orientacao,tamnho):
    posicoes = []
    if orientacao =='H':
        for i in range(tamnho):
            posicoes.append((linha,coluna + i))
    elif orientacao =='V':
        for i in range(tamnho):
            posicoes.append((linha + i,coluna))
    return posicoes