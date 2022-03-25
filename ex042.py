r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if (r1 + r2) > r3 and (r1 + r3) > r2 and (r2 + r3) > r1:
    print('Esses três segmentos podem formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO.(Todos os lados iguais)')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.(Possue todos lados diferentes)')
    else:
        print('ISÓSCELES.(Possue dois lados iguais)')
else:
    print('Esses três segmentos não podem formar um triângulo.')
