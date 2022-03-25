from datetime import date
at = date.today().year
a = int(input('Digite o ano de nascimento: '))
i = at - a
print('Quem nasceu em {} tem {} anos em {}.'.format(a, i, at))
if i < 18:
    print('Você ainda vai se alistar no serviço militar!Ainda falta {} ano(s).'.format(18 - i))
    print('O ano do seu alistamento será em {}.'.format(at + (18 - i)))
elif i == 18:
    print('Você deve se alistar no serviço militar essa ano!')
elif i > 18:
    print('Já passou o ano do seu alistamento militar. Foi há {} ano(s).'.format(i- 18))
    print('O ano do seu alistamento foi em {}.'.format(at - (i-18)))
