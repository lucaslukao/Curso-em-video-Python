a = 0
b = 0
hm = ''
f = 0
for c in range(1, 5):
    print('----- {}ºPessoa -----'.format(c))
    n = str(input('Nome: ')).strip()
    i = int(input('Idade: '))
    a += i   # Para calcular a média das idades
    s = str(input('Sexo [M/F]: ')).strip()
    # Analisa quem é o homem mais velho
    if c == 1 and s in 'Mm':
        b = i
        hm = n
    elif s in 'Mm' and i > b:
        b = i
        hm = n

    # Analisa quantas mulheres tem menos de 20 anos
    if s in 'Ff' and i < 20:
        f += 1
print('''A média da idade do grupo é {:.0f} anos.
O homem mais velho tem {} e se chama {}.
O número de mulheres com menos de 20 anos é {}.'''.format(a / 4, b, hm, f))
