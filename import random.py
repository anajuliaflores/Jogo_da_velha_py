import random

def exibe_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print('|'.join(linha))
        print('-' * 11)

def movimento_humano(tabuleiro, player):
    while True:
        try:
            linha = int(input('Escolha a linha (0, 1, 2): '))
            coluna = int(input('Escolha a coluna (0, 1, 2): '))
            if tabuleiro[linha][coluna] == '   ':
                tabuleiro[linha][coluna] = player
                break
            else:
                print('Esta casa está ocupada, tente outra!')
        except (ValueError, IndexError):
            print('Entrada inválida! Utilize apenas números entre 0 e 2.')

def movimento_bot(tabuleiro, player):
    print(f'Turno do Bot {player}')
    while True:
        linha = random.randint(0, 2)
        coluna = random.randint(0, 2)
        if tabuleiro[linha][coluna] == '   ':
            tabuleiro[linha][coluna] = player
            break

def verificar_vitoria(tabuleiro, player): 
    for linha in tabuleiro:
        if all(celula == player for celula in linha):
            return True

    for coluna in range(3):
        if all(tabuleiro[linha][coluna] == player for linha in range(3)):
            return True

    if all(tabuleiro[i][i] == player for i in range(3)):
        return True
    if all(tabuleiro[i][2 - i] == player for i in range(3)):
        return True

    return False

def verificar_empate(tabuleiro):
    return all(celula != '   ' for linha in tabuleiro for celula in linha)

tabuleiro = [
    ['   ', '   ', '   '],
    ['   ', '   ', '   '],
    ['   ', '   ', '   ']
]

player = ' X '

while True:
    print(f'Turno do Jogador {player}')
    exibe_tabuleiro(tabuleiro)
    
    if player == ' X ':
        movimento_humano(tabuleiro, player)
    else:
        movimento_bot(tabuleiro, player)

    if verificar_vitoria(tabuleiro, player):
        exibe_tabuleiro(tabuleiro)
        print(f'Jogador {player} venceu!')
        break

    if verificar_empate(tabuleiro):
        exibe_tabuleiro(tabuleiro)
        print('Empate!')
        break

    player = ' O ' if player == ' X ' else ' X '

