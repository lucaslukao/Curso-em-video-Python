from time import sleep
escolha = 0
v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
print('Segue abaixo algumas opções:')
while escolha != 5:
    sleep(1)
    escolha = int(input('''[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair do programa 
>Qual a sua escolha? '''))
    if escolha == 1:
        print('{} + {} = {}.'.format(v1, v2, v1 + v2))
        print('=-=' * 10)
    elif escolha == 2:
        print('{} x {} = {}.'.format(v1, v2, v1 * v2))
        print('=-=' * 10)
    elif escolha == 3:
        if v1 > v2:
            print('O moir valor é {}.'.format(v1))
            print('=-=' * 10)
        elif v1 < v2:
            print('O maoir valor é {}.'.format(v2))
            print('=-=' * 10)
        else:
            print('Os valores são iguais.')
            print('=-=' * 10)
    elif escolha == 4:
        v1 = int(input('Digite um número: '))
        v2 = int(input('Digite outro número: '))
        print('=-=' * 10)
    elif escolha == 5:
        escolha = 5
    else:
        print('Opção inválida! Tente novamente.')
        print('=-=' * 10)
print('Finalizando...')
sleep(2)
print('=-=' * 10)
print('Fim do programa! Volte sempre!')
