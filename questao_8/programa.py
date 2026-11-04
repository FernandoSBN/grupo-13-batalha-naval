from funcoes import *

frota = {}
navios = [
    ('porta-aviões', 4, 1),
    ('navio-tanque', 3, 2),
    ('contratorpedeiro', 2, 3),
    ('submarino', 1, 4),
]

for nome, tamanho, quantidade in navios:
    for i in range(quantidade):
        print(f'Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}')
        valido = False
        while not valido:
            linha = int(input('Linha: '))
            coluna = int(input('Coluna: '))
            orientacao = 'vertical'
            if tamanho > 1:
                op = int(input('[1] Vertical [2] Horizontal > '))
                if op == 2:
                    orientacao = 'horizontal'

            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valido = True
            else:
                print('Esta posição não está válida!')

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}

tabuleiro_oponente = posiciona_frota(frota_oponente)
tabuleiro_jogador = posiciona_frota(frota)

jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    linha = int(input('Jogador, qual linha deseja atacar? '))
    while linha < 0 or linha > 9:
        print('Linha inválida!')
        linha = int(input('Jogador, qual linha deseja atacar? '))

    coluna = int(input('Jogador, qual coluna deseja atacar? '))
    while coluna < 0 or coluna > 9:
        print('Coluna inválida!')
        coluna = int(input('Jogador, qual coluna deseja atacar? '))

    if tabuleiro_oponente[linha][coluna] in ('X', '-'):
        print(f'A posição linha {linha} e coluna {coluna} já foi informada anteriormente!')
        continue

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False