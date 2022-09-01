valores = list()
posmaior = list()
posmenor = list()
for c in range(0, 5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
for posicao, numero in enumerate(valores):
    if numero == max(valores):
        posmaior.append(posicao)
    if numero == min(valores):
        posmenor.append(posicao)
print(f'''O maior valor é {max(valores)} nas posições {posmaior}.
O menor valor é {min(valores)} nas posições {posmenor}.''')
