# Calculando seno, cosseno e tangente
from math import radians, sin, cos, tan
an = float(input('Digite o valor do ângulo: '))
print(f'''O valor do seno é {sin(radians(an)):.2f}
O valor do cosseno é {cos(radians(an)):.2f}
O valor da tangente é {tan(radians(an)):.2f}''')

