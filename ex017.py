# Calculando a hipotenusa

# Sem usar bibliotecas
# ca = float(input('Digite o valor do cateto adjacente: '))
# co = float(input('Digite o valor do cateto oposto: '))
# print(f'O comprimento da hipotenusa é {(ca**2 + co**2) ** (1/2) :.2f}')


# Usando biblioteca
from math import hypot
ca = float(input('Digite o cateto adjacente: '))
co = float(input('Digite o cateto oposto: '))
print(f'O valor da hipotenusa é {hypot(ca, co)}')
