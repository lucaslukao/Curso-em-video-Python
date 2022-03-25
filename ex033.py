a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))
# Verificando qual é o menor
menor = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c
# Verficando qual é o maoir
maior = b
if a > b and a > c:
    maior = a
if c > b and c > a:
    maior = c
print('O número {} é o menor.'.format(menor))
print('O número {} é o maior.'.format(maior))
