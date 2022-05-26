s = str(input('Qual o seu sexo?( Digite [M] para masculino e [F] para feminino) ')).strip().upper()[0]  # Pega só a primeira letra
while s not in 'MF':
    s = str(input('Resposta inválida! Digite [M] para masculino e [F] para feminino: ')).strip().upper()[0]
