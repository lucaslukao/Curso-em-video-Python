while True:
    n = int(input('Digite um número: '))
    print('=' * 20)
    print('[1] = Binário.\n[2] = Octal\n[3] = Hexadecimal')
    o = int(input("Digite para qual base você quer converter, das opções acima: "))
    if o == 1:
        print('{} convertido para binário é igual a {}'.format(n, bin(n)[2:]))
    elif o == 2:
        print('{} convertido para octal é igual a {}'.format(n, oct(n)[2:]))
    elif o == 3:
        print('{} convertido para hexadecimal é igual a {}'.format(n, hex(n)[2:]))
    else:
        print('Opção inválida! Tente novamente.')