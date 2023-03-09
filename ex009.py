# Tabuáda
n = int(input('Digite um número para ver sua tabuada: '))
c = 0
for c in range(0, 11):
    print(f'{n} x {c:2} = {n*c}')
    c += 1
