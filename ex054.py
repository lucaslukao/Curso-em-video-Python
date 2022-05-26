from datetime import date
a = date.today().year
m = 0
n = 0
for c in range(1, 8):
    i = int(input('Digite o ano de nascimento da {} pessoa: '.format(c)))
    if a - i >= 21:
        m += 1
    else:
        n += 1
print('O número de pessoas e maiores de idade é {} e o de menores é {}.'.format(m, n))
