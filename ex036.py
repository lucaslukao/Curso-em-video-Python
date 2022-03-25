v = float(input('Qual o valor da casa que você deseja comprar?R$ '))
s = float(input('Qual o seu salário?R$ '))
t = float(input('Em quantos anos você vai pagar a casa? '))
p = v / (t * 12)
if p > s * 0.3:
    print('\033[31mEMPRÉSTIMO NEGADO!\033[mO valor da prestação mensal não pode ultrapassar 30% do seu salário.')
    print('Valor da prestação: R${:.2f}'.format(p))
else:
    print('\033[36mEMPRÉSTIMO CONCEDIDO!\033[mO valor da prestação mensal será de R${:.2f}'.format(p))
