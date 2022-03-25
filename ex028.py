from random import randint
print('Pensando em um número de 0 a 5 ...')
n1 = randint(0, 5) # Faz o computador pensar
n2 = int(input('Qual número você acha que foi escolhido? ')) # O jogador tenta andivinhar
if n2 == n1:
    print('Você venceu!')
else:
    print('Você perdeu! O número era {}.'.format(n1))

