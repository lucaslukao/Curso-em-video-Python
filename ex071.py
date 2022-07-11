cinquenta = vinte = dez = um = 0
print('-' * 20)
print('{:^20}'.format('CAIXA ELETRÔNICO'))
print('-' * 20)
valor = int(input('Qual valor deseja sacar?R$ '))
while True:
    if valor >= 50:
        valor -= 50
        cinquenta += 1
    elif valor >= 20:
        valor -= 20
        vinte += 1
    elif valor >= 10:
        valor -= 10
        dez += 1
    elif valor >= 1:
        valor -= 1
        um += 1
    elif valor == 0:
        break
print(f'Total de {cinquenta} cédulas de R$50.')
print(f'Total de {vinte} cédulas de R$20.')
print(f'Total de {dez} cédulas de R$10.')
print(f'Total de {um} cédulas de R$1.')
print('-' * 20)
print('Volte sempre!')