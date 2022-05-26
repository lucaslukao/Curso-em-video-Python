n = int(input('Digite um número: '))
s = 0
for c in range(1, n + 1):
    if n % c == 0:
        s += 1
if s == 2:
    print('{} é primo'.format(n))
else:
    print('{} não é primo.'.format(n))
