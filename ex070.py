total =contm = contb = 0
print('-' * 20)
print('PROGRAMA DE LOJINHA')
print('-' * 20)
while True:
    nome = str(input('Qual o nome do produto? '))
    valor = float(input('Qual o preço do produto?R$ '))
    if valor >= 1000:
        contm += 1
    total += valor
    final = ' '
    while final not in 'SN':
        final = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    print('-' * 20)
    if final == 'N':
        print('FIM DO PROGRAMA!')
        print(f'O total da compra é {total}.')
        print(f'{contm} custam mais de R$1000.00.')
        break
