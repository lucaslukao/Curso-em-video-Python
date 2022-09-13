dados = list()
temp = dict()
média = 0
while True:
    temp['nome'] = str(input('Nome: '))
    while True:
        temp['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if temp['sexo'] in 'MF':
            break
    temp['idade'] = int(input('Idade: '))
    média += temp['idade']
    dados.append(temp.copy())
    while True:
        conf = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if conf in 'NS':
            break
        print('ERRO! Digite apenas S ou N!')
    if conf == 'N':
        break
média = média / len(dados)
print(dados)
print('=-' * 20)
print(f'- O grupo tem {len(dados)} pessoas.')
print(f'- A idade média é {média:.2f}.')
print('- As mulheres foram: ', end='')
for c in dados:
    if c['sexo'] == 'F':
        print(c['nome'], end=' ')
print()
print('- Lista de pessoas que estão acima da média:')
for c in dados:
    if c['idade'] >= média:
        print('  ', end='')
        for k, v in c.items():
            print(k, '=', v, end='; ')
        print()
