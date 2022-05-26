print('SEQUÊNCIA DE FIBONACCI')
print('=-' * 30)
n = int(input('Digite um número: '))
cont = 2
v1 = 0
v2 = 1
print('=-' * 30)
print('{} -> {} -> '.format(v1, v2,), end='')
while cont < n:
    f = v1 + v2
    print(f, end=' -> ')
    v1 = v2
    v2 = f
    cont += 1
print('FIM')
print('\nEsses foram os {} primeiros elementos da sequência de Fibonacci.'.format(n))
print('=-' * 30)
