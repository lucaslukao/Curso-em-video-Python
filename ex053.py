f = str(input('Digite uma frase para ver se ela é um palíndromo: ')).strip().upper()
palavras = f.split()
junto = ''.join(palavras)
inverso = junto[:: -1]
# inverso = ''
# for letra in range(len(junto) - 1, -1, -1):
#     inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('Não é um palíndromo!')
