# Sorteando um aluno

import random
alunos = [str(input('Digite o nome do 1° aluno: ')),
          str(input('Digite o nome do 2º aluno: ')),
          str(input('Digite o nome do 3° aluno: ')),
          str(input('Digite o nome do 4° aluno: '))]
print(f'{random.choice(alunos)}, foi selecionado(a)!')
