from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = hypot(co, ca)
print('O valor da hipotenusa é {:.2f}.'.format(h))
'''h = (ca**2 + co**2) **(1/2)
print('O valor da hipotenusa é {:.2f}.'.format(h))'''
