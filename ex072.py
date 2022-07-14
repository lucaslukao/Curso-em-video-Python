tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'catorze', 'quinze',
         'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            print(f'Você digitou o número {tupla[num]}.')
            break
        print('Tente novamente. ', end='')
    resp = str(input('Quer continuar?[S/N] ')).strip().upper()
    while resp not in 'NS':
        resp = str(input('Quer continuar?[S/N] ')).strip().upper()
    if resp == 'N':
        break
