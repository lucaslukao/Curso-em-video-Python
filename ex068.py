from random import randint
contv = 0
print('JOGO DO ÍMPAR OU PAR.')
while True:
    print('-_' * 20)
    player = int(input('Digite um número: '))
    pi = ' '
    while pi not in 'PI':
        pi = str(input('Par ou impar? [P/I] ')).strip().upper()[0]
    a = randint(0, 11)
    if pi == 'P':
        if (player + a) % 2 == 0:
            print(f'Jogador venceu! A escolha do computador foi {a}.')
            contv += 1
        elif (player + a) % 2 != 0:
            print(f'Fim do jogo! A escolha do computador foi {a}. Você venceu {contv} partidas.')
            break
    elif pi == 'I':
        if (player + a) % 2 != 0:
            print(f'Jogador venceu! A escolha do computador foi {a}.')
            contv += 1
        elif (player + a) % 2 == 0:
            print(f'Fim do jogo! A escolha do computador foi {a}. Você venceu {contv} partidas.')
            break
