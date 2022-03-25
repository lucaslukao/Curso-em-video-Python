r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro: '))
if (r1 + r2) > r3 and (r2 + r3) > r1 and (r3 + r1) > r2:
    print('Devido a condição de existência de um triângulo, essas três retas podem formar um triângulo.')
else:
    print('Devido a condição de existência de um triângulo, essas três retas não podem formar um triângulo.')