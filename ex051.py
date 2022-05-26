t1 = int(input('Digite o primeiro termo de uma PA: '))
r = int(input('Digite a razão dessa PA: '))
for c in range(t1, t1 + 11):
    print(t1, end=' -> ')
    t1 += r
print('Esses foram os 10 primieros números dessa PA')
