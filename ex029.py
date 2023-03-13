carro = float(input('Qual a velocidade do carro? '))
if carro > 80:
    print(f'''MULTADO! O limite da velocidade é 80km.
O valor da multa é R${(carro - 80) * 7:.2f}''')
else:
    print('Tudo certo! Carro na velocidade correta.')
