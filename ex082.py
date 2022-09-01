valor = []
par = []
impar = []
while True:
    valor.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
for c, i in enumerate(valor):
    if i % 2 == 0:
        par.append(valor[c])
    else:
        impar.append(valor[c])
print('-=' * 20)
print(f'Você digitou tais valores {valor}.')
print(f'Os valores pares são {par}.')
print(f'Os valores impares são {impar}.')
