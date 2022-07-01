total = 0
print('-' * 20)
print('PROGRAMA DE LOJINHA')
print('-' * 20)
while True:
    nome = str(input('Qual o nome do produto? '))
    valor = float(input('Qual o preço do produto?R$ '))
    total += valor
    final = ' '
    while final not in 'SN':
        final = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    if final == 'N':
        print('FIM DO PROGRAMA!')
        print(f'O total da compra é {total}')
        break
