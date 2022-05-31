cont = conts = m = n = 0
p = 'S'
while p != 'N':
    s = int(input('Digite um valor: '))
    p = str(input('Deseja continuar?[S/N] ')).strip().upper()[0]
    conts += s
    cont += 1
    if cont == 1:
        m = n = s
    else:
        if s > m:
            m = s
        elif s < n:
            n = s
print('''A média entre os números digitados foi de {:.2f}
O maoir valor foi {}, e o menor foi {}.'''.format(conts/cont, m, n))
