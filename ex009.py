n = int(input('Digite um número: '))
a = 0
print('\033[36m-\033[m'*20)
while a <= 10:
    print('{}{} x {:2} = {}{}'.format('\033[7;30;41m', n, a, a*n, '\033[m'))
    a += 1
print('\033[36m-\033[m' * 20)
