from random import randint
from time import sleep
laço = int(input('Quantos jogos você deseja sortear? '))
temp = list()
for c in range(0, laço):
    while len(temp) != 6:
        num = randint(1, 60)
        if num not in temp:
            temp.append(num)
    print(f'Jogo {c + 1}: {temp}')
    temp.clear()
    sleep(1)
