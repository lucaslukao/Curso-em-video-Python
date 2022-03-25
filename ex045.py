from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[0] - PEDRA
[1] - PAPEL
[2] - TESOURA''')
jogador = int(input('Qual a sua escolha? '))
print('_-' * 10)
print('''O computador jogou {}
Jogador jogou {}'''.format(itens[computador], itens[jogador]))
print('_-' * 10)
if computador == 0: # O computador jogou pedra
    if jogador == 0:
        print('EMPATE.')
    elif jogador == 1:
        print('JOGADOR VENCE!!!')
    elif jogador == 2:
        print("COMPUTADOR VENCE!")
    else:
        print('Jogada INVÁLIDA!!! Tente novamente')
elif computador == 1: # O computador jogou papel
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!!!')
    else:
        print('JOGADA INVÁLIDA! Tente novamente.')
elif computador == 2: # O computador jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCE!!!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('JOGADA INVÁLIDA! Tente novamente.')