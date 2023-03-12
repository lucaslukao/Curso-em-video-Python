from random import shuffle
alunos = [str(input('1º aluno: ')),
          str(input('2ª aluno: ')),
          str(input('3º aluno: ')),
          str(input('4º aluno: '))]
shuffle(alunos)
print(f'A ordem da apresentação é: \n {alunos}')
