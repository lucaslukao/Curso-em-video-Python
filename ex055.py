a = 0
b = 0
for c in range(1, 6):
    p = float(input('Qual o peso da {}º pessoa?kg '.format(c)))
    if c == 1:
        a = p
        b = p
    else:
        if p > a:
            a = p
        elif p < b:
            b = p
print('O maior peso foi {}kg e o menor foi {}kg'.format(a, b))
