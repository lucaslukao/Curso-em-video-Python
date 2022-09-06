geral = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    média = (nota1 + nota2) / 2
    geral.append([nome, [nota1, nota2], média])
    confir = str(input('Deseja continuar? [S/N] '))
    if confir in 'Nn':
        break
print('=-' * 20)
print(f'{"Nu.":<4}{"Nome":<10}{"Média":>8}')
for i, l in enumerate(geral):
    print(f'{i:<4}{l[0]:<10}{l[2]:>8}')
print('=-' * 20)
while True:
    aluno = int(input('Deseja ver as notas de qual aluno? [999 finaliza] '))
    if aluno == 999:
        break
    if aluno <= len(geral) - 1:
        print(f'As notas de {geral[aluno][0]} são: {geral[aluno][1]}.')
print('PROGRAMA FINALIZADO!')
