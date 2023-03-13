km = float(input('Qual a distância da viagem?(Km) '))
print(f'O valor da viagem é R${km * 0.45 if km <= 200 else km * 0.5:.2f}.')
