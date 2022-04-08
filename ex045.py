from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA''')
jogador = int(input('Qual a sua escolha? '))
if jogador <= 2:
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print('_-' * 20)
    print('''O computador jogou {}\nJogador jogou {}'''.format(itens[computador], itens[jogador]))
    print('_-' * 20)
    if computador == 0:   # O computador jogou pedra
        if jogador == 0:
            print('EMPATE.')
        elif jogador == 1:
            print('JOGADOR VENCE!!!')
        else:
            print("COMPUTADOR VENCE!")
    elif computador == 1:    # O computador jogou papel
        if jogador == 0:
            print('COMPUTADOR VENCE!')
        elif jogador == 1:
            print('EMPATE!')
        else:
            print('JOGADOR VENCE!!!')
    elif computador == 2:   # O computador jogou tesoura
        if jogador == 0:
            print('JOGADOR VENCE!!!')
        elif jogador == 1:
            print('COMPUTADOR VENCE!')
        else:
            print('EMPATE!')
else:
    print('Jogada inválida!')
