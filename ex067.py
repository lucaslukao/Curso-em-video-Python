while True:
    n = int(input('Qual número deseja ver a tabuada? '))
    cont = 1
    if n < 0:
        print('Programa finalizado!')
        break
    while cont <= 10:
        print(f'{n} x {cont} = {n * cont}')
        cont += 1
