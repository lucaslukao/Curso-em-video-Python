f = str(input('Digite uma frase: ')).strip().lower()
print('A letra "a" aparece {} veze(s) \nA posição em que ela aparece pela primeira vez é {} \nA última posicão que ela apareceu foi: {}'.format(f.count('a'), f.find('a') + 1, f.rfind('a') + 1 ))
