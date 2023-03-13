# Menor e maior de 3 números

# Minha solução
# n1 = float(input('Digite o 1º valor: '))
# n2 = float(input('Digite o 2° valor: '))
# n3 = float(input('Digite o 3° valor: '))
# maior = 0
# menor = 0
# if n1 > n2:
#     if n1 > n3:
#         maior = n1
#         if n3 > n2:
#             menor = n2
#         else:
#             menor = n3
#     else:
#         maior = n3
#         menor = n2
# else:
#     if n2 > n3:
#         maior = n2
#         if n1 > n3:
#             menor = n3
#         else:
#             menor = n1
#     else:
#         maior = n3
#         menor = n1
# print(f'''O maior é {maior}.
# O menor é {menor}.''')

# Solução do Guanabara
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
elif c > b and c > a:
    maior = c
print('O número {} é o menor.'.format(menor))
print('O número {} é o maior.'.format(maior))
