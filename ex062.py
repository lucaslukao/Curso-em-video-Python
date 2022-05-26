print('GERADOR DE PA')
print('=-=' * 10)
t1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
termo = t1
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? ([ 0 ] para finalizar o programa). '))
#     print(t1, end=' -> ')
#     t1 += r
#     c += 1
# print('Esses foram os primeiros 10 números dessa PA.')
# c2 = int(input('''Digite a quantidade de termos que você deseja ver.
# Caso queira finalizar o programa, digite [0].
# '''))
# while c2 > 0:
#     print(t1, end=' -> ' if c2 > 1 else '\n')
#     t1 += r
#     c2 -= 1
#     if c2 == 0:
#         print('=-=' * 10)
#         c2 = int(input('Quantidades de termos?([0] para finalizar o programa): '))
print('Programa finalizado.')
