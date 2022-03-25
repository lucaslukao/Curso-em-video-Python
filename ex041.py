from datetime import date
an = int(input('Digite o ano do nascimento: '))
i = date.today().year - an
print('Esse atleta tem, ou terá, {} anos.'.format(i))
if i <= 9:
    print('Sua categoria é MIRIM.')
elif i <= 14:
    print('Sua categoria é INFANTIL.')
elif i <= 19:
    print('Sua categoria é JUVENIL.')
elif i <= 25:
    print('Sua categoria é SÊNIOR.')
else:
    print('Sua categoria é MASTER.')
