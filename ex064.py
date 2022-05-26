contn = conts = 0
cont = int(input('Digite um número[999 para parar]: '))
while cont != 999:
    contn += 1
    conts += cont
    cont = int(input('Digite um número[999 para parar]: '))
print('''A quantidade de números digitados até atingir a flag foi de {}.
A soma entre eles, excluíndo a flag, foi de {}.'''.format(contn, conts))
