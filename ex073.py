tabela = ('SE Palmeiras SP', 'Corinthians SP', 'Internacional RS', 'Atlético Mineiro', 'Fluminense RJ',
          'Atlético Paranaense', 'São Paulo FC SP', 'Santos FC SP', 'CR Flamengo RJ', 'Botafogo FR RJ',
          'Red Bull Bragantino SP', 'Goiás EC GO', 'Cuiaba Esporte Clube MT', 'Coritiba FC PR', 'América FC MG',
          'Avaí FC SC', 'Ceará SC CE', 'Atlético Goianiense', 'EC Juventude RS', 'Fortaleza-CE')
print('=' * 30)
print(f'Lista de times: {tabela}')
print('=' * 30)
print(f'Os 5 primeiros colocados são: {tabela[0:5]}')
print('=' * 30)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('=' * 30)
print(f'Os times em ordem alfabética é: {sorted(tabela)}')
print('=' * 30)
print(f'O Atlético Mineiro está na {tabela.index("Atlético Mineiro") + 1}º posição')
