# Vereficando se o ano é bissexto.

# Minha solução:
# ano = int(input('Digite um ano para saber se é bissexto: '))
# if ano % 4 == 0:
#     if ano % 100 == 0:
#         if ano % 400 == 0:
#             print(f'O ano {ano} é bissexto.')
#         else:
#             print(f'O ano {ano} não é bissexto.')
#     else:
#         print(f'O ano {ano} é bissexto.')
# else:
#     print(f'O ano {ano} não é bissexto')

# Solução do guanabara:
from datetime import date
a = int(input('Que ano quer analisar, para saber se é bissexto? Digite 0 para saber o atual: '))
if a == 0:
    a = date.today().year
an = 'é bissexto' if a % 4 == 0 and a % 100 != 0 or a % 400 == 0 else 'não é bissexto'
print('O ano {} {}'.format(a, an))
