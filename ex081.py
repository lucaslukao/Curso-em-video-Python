lista = []
while True:
    lista.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
    while resp not in 'SN':
        resp = str(input('Valor inválido!!! Quer continuar? [S/N] ')).strip().upper()
    if resp == 'N':
        break
print('=-' * 20)
print(f'- No total, foram digitados {len(lista)} valores.')
lista.sort(reverse=True)
print(f'- A ordem decrescente é {lista}')
if 5 in lista:
    print('- O número 5 está na lista.')
else:
    print('- O valor 5 não foi encontrado na lista.')
