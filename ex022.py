n = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em letra maiúscula é {}'.format(n.upper()))
print('Seu nome em letras minúsculas é {}'.format(n.lower()))
print('Seu nome tem ao todo {} letra(s)'.format(len(n) - n.count(' ')))
n = n.split()
print('O seu primeiro nome é {} e tem {} letra(s). '.format(n[0], len(n[0])))
#print('O seu primeiro nome tem {} letra(s)'.format(n.find(' ')))
