print('GERADOR DE PA')
print('=-=' * 10)
t1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))
c = 0
while c < 10:
    print(t1, end=' -> ')
    t1 += r
    c += 1
print('Esses foram os primeiros 10 números dessa PA.')

