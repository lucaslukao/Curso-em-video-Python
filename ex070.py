total = contm = contmen = tot =  0
menor = ' '
print('-' * 20)
print('PROGRAMA DE LOJINHA')
print('-' * 20)
while True:
    nome = str(input('Qual o nome do produto? ')).strip()
    valor = float(input('Qual o preço do produto?R$ '))
    tot += 1
    if tot == 1 or valor < contmen:
        contmen = valor
        menor = nome
    if valor >= 1000:
        contm += 1
    total += valor
    final = ' '
    while final not in 'SN':
        final = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    print('-' * 20)
    if final == 'N':
        print('FIM DO PROGRAMA!')
        print(f'O total da compra é R${total:.2f}.')
        print(f'{contm} custam mais de R$1000,00.')
        print(f'O produto mais barato é {menor}, pelo preço de R${contmen:.2f}.')
        break
