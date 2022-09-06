matriz =[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = somac = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
    print()
print('-=' * 20)
print(f'A soma dos valores pares é {somap}')
for c in range(0, 3):
    somac += matriz[c][2]
print(f'A soma dos valores da terceira coluna é {somac}')
print(f'O maoir valor da segunda linha é {max(matriz[1])}')
