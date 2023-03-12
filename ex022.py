nome = input('Digite seu nome completo: ').strip()
print(f'''O seu nome em maiúsculo é: {nome.upper()}
Em minúsculo: {nome.lower()}
Seu nome tem {len(nome) - nome.count(' ')} letras no total.
O seu primeiro nome é {nome.split()[0].upper()} e tem  {len(nome.split()[0])} letras.''')
