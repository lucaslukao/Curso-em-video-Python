print('-' * 20)
print('CADASTRE UMA PESSOA')
conti = conth = contm = 0
while True:
    print('-' * 20)
    i = int(input('Idade: '))
    if i >= 18:
        conti += 1
    s = ' '
    while s not in 'MF':
        s = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if s == 'M':
        conth += 1
    if s == 'F' and i < 20:
        contm += 1
    print('-' * 20)
    b = ' '
    while b not in 'SN':
        b = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if b == 'N':
        print('FIM DO PROGRAMA!')
        print(f'''Tem {conti} pessoas com mais de 18 anos.
Foram cadastrados {conth} homens.
{contm} mulheres tem menos de 20 anos.''')
        break
