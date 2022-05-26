a = 0
o = 0
for c in range(1, 7):
    n = int(input('Digite o {} número: '.format(c)))
    if n % 2 == 0:
        a += n
        o += 1
print('A soma dos {} números pares foi de {}'.format(o, a))
