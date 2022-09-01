lista = list()
temp = list()
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso[kg]: ')))
    if len(lista) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]

    confir = str(input('Deseja continuar? [S/N] ')).strip().upper()
    lista.append(temp[:])
    temp.clear()
    if confir == 'N':
        break
print(f'Foram cadastradas {len(lista)} pessoas.')

print(f'O maior peso foi {maior[0][1]}. Peso de ', end='')
for c in maior:
    print(c[0], end=', ')
print(f'\nO menor peso foi de {menor[0][1]}. Peso de ', end='')
for c in menor:
    print(c[0], end=', ')
