n = str(input('Sigite uma frase: ')).strip().upper()
print(f'''A letra [A] aparece {n.count("A")} vezes.
A primeira posição é {n.find('A') + 1}
A segunda em {n.rfind('A') + 1}.''')
