s = float(input('Digite o seu salário atual: R$'))
if s > 1250:
    s = s * 0.1 + s
    print('O seu aumento é de 10%, logo seu salário é de R${}'.format(s))
else:
    s = s * 0.15 + s
    print('O seu aumento é de 15%, logo seu sálario é de R${}'.format(s))
