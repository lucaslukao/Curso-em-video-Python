s = cont = 0
while True:
    n = int(input('Digite um valor [999 para finalizar]: '))
    if n == 999:
        break
    s += n
    cont += 1
print(f'Foi digitado {cont} valores e a soma entre eles é {s}.')
