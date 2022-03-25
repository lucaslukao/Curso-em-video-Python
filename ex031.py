d = float(input('Qual a distância da viagem?Km: '))
preco = d * 0.5 if d <= 200 else d * 0.45
print('Você está preste a começar uma viagem de {}km, cujo preço é {}'.format(d, preco))
