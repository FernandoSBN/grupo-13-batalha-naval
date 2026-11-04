from funcoes import *

frota = {}
nomes = ["porta-aviões", "navio-tanque", "contratorpedeiro", "submarino"]
quantidades = [1, 2, 3, 4]
tamanhos = [4, 3, 2, 1]

for i in range(len(nomes)):
    nome = nomes[i]
    tamanho = tamanhos[i]
    for k in range(quantidades[i]):
        valido = False
        while not valido:
            print(f"Insira as informações referentes ao navio {nome} que possui tamanho {tamanho}")
            linha = int(input("Linha: "))
            coluna = int(input("Coluna: "))
            if tamanho == 1:
                orientacao = "horizontal"
            else:
                escolha = int(input("Orientação: [1] Vertical [2] Horizontal "))
                if escolha == 1:
                    orientacao = "vertical"
                else:
                    orientacao = "horizontal"
            if posicao_valida(frota, linha, coluna, orientacao, tamanho):
                frota = preenche_frota(frota, nome, linha, coluna, orientacao, tamanho)
                valido = True
            else:
                print("Esta posição não está válida!")

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

total_navios = 0
for nome in frota_oponente:
    total_navios += len(frota_oponente[nome])

jogando = True
while jogando:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))

    repetida = True
    while repetida:
        linha = int(input("Jogador, qual linha deseja atacar? "))
        while linha < 0 or linha > 9:
            print("Linha inválida!")
            linha = int(input("Jogador, qual linha deseja atacar? "))

        coluna = int(input("Jogador, qual coluna deseja atacar? "))
        while coluna < 0 or coluna > 9:
            print("Coluna inválida!")
            coluna = int(input("Jogador, qual coluna deseja atacar? "))

        if tabuleiro_oponente[linha][coluna] == 'X' or tabuleiro_oponente[linha][coluna] == '-':
            print(f"A posição linha {linha} e coluna {coluna} já foi informada anteriormente!")
        else:
            repetida = False

    tabuleiro_oponente = faz_jogada(tabuleiro_oponente, linha, coluna)

    if afundados(frota_oponente, tabuleiro_oponente) == total_navios:
        print("Parabéns! Você derrubou todos os navios do seu oponente!")
        jogando = False