# Jogo para adivinhar qual número o computador 'pensou'
from random import randint
jogador = int(input('''O computador chutou um número entre 0 e 5. 
Consegue adivinhar qual? '''))
computador = randint(0, 5)
if jogador == computador:
    print('Parabéns! Você acertou!')
else:
    print(f'Errado! O computador chutou {computador}.')
