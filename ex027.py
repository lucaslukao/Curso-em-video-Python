nome = str(input('Digite seu nome: ')).title().strip().split()
print(f'''Seu primeiro nome é {nome[0]}.
O seu último é {nome[len(nome) - 1]}.''')
