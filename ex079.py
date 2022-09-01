lista = list()
while True:
    valor = (int(input('Digite um valor: ')))
    if valor in lista:
        print('O valor já está presente na lista, não sera adicionado novamente.')
    else:
        lista.append(valor)
        print('Valor adicionado com sucesso')
    decisao = str(input('Deseja continuar?[S/N] ')).strip().upper()
    while decisao not in 'SN':
        decisao = str(input('Deseja continuar?[S/N] ')).strip().upper()
    if decisao == 'N':
        break
print(sorted(lista))

