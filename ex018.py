from math import radians, sin, cos, tan
a = float(input('Digite o valor do ângulo: '))
print('O valor do seno é {:.2f} \nO valor do cosseno é {:.2f} \nO valor da tangente é {:.2f}'.format(sin(radians(a)), cos(radians(a)), tan(radians(a))))
