p = float(input('Qual o valor do produto?R$ '))
print('''[1] - À vista(10% de desconto)
[2] - À vista no cartão(5% de desconto)'
[3] - 2x no cartão(preço normal)
[4] - 3x ou mais no cartão(20% de juro)''')
c = int(input('Qual a condição de pagamento? '))
if c == 1:
    print('O valor a ser pago é R$ {:.2f}'.format(p - (p * 0.1)))
elif c == 2:
    print('O valor a ser pago é R$ {:.2f}'.format(p - (p * 0.05)))
elif c == 3:
    print('O valor a ser pago é R$ {:.2f}'.format(p))
elif c == 4:
    parc = int(input('Quantas parcelas? '))
    print('O valor a ser pago é R$ {:.2f} (COM JUROS), em parcelas de R$ {:.2f}.'.format(p + (p * 0.2), p / parc))
