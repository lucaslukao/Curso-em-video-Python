n1 = float(input('Digite o valor da primeira nota: '))
n2 = float(input('Digite o valor da segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('\033[31mREPROVADO!\033[m')
elif 7 > m >= 5:
    print('\033[33mRECUPERAÇÃO!\033[m')
elif m >= 7:
    print('\033[36mAPROVADO!\033[m')
