from random import randint
from time import sleep
print('Pensando em número de 0 a 10 ', end='')
for c in range(0, 3):
    sleep(1)
    print('.', end='')
n1 = randint(0, 10)
sleep(1)
a = False
p = 0
while not a:
    j = int(input('\nTente adivinhar o número que o computador pensou: '))
    p += 1
    if j == n1:
        a = True
    else:
        if j < n1:
            print('É um número maoir.')
        elif j > n1:
            print('É um número menor.')
print('''Parabéns, você acertou!!! 
O número que o computador pensou foi {} e você precisou de {} tentativas para advinhar'''.format(n1, p))
