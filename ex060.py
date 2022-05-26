n = int(input('Digite um valor: '))
c = n
t = 1
print('A fatorial de {}! = '.format(n), end='')
while c > 0:
    print(' {} '.format(c), end='')
    print('x' if c > 1 else '= ', end='')
    t *= c
    c -= 1
print(t)
