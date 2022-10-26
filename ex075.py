valores = (int(input('1° valor: ')), int(input('2° valor: ')),
           int(input('3° valor: ')), int(input('4° valor: ')))
print(f'O valor 9 apareceu {valores.count(9)} vezes')
print(f'A posição {valores.index(3)} foi a primeira em que o 3 aparaceu.' if 3 in valores else '3 não foi digitado.')
print('Os valores pares foram: ', end='')
c = 0
for k, v in enumerate(valores):
    if valores[k] % 2 == 0:
        print(v, end=' ')
    else:
        c += 1
        if c == 4:
            print('nenhum')
