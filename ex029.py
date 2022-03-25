v = float(input('Qual a velocidade atual do carro?km: '))
if v > 80:
    v2 = (v - 80) * 7
    print('Multado! O carro está acima do limite de velocidade, que é 80 km/h. O valor da multa é: R${:.2f}'.format(v2))
else:
    print('Tenha um bom dia e dirija com segurança')