tupla = (int(input('Digite um valor: ')), int(input('Digite outro valor: ')),
         int(input('Digite mais um valor: ')), int(input('Digite o último valor: ')))
print(f'O valor 9 apareceu {tupla.count(9)} vezes.')
print(f'O primeiro valor 3 está na posiçã {tupla.index(3) + 1}.')if 3 in tupla else print('O valor 3 não foi digitado.')
print('Os valores pares foram', end=' ')
b = 0
for t in tupla:
    if t % 2 == 0:
        print(t, end=' ')
    else:
        b += 1
        if b == 4:
            print('nenhum')
