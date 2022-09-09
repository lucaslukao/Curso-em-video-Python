from datetime import datetime
registro = dict()
registro['nome'] = str(input('Nome: '))
registro['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
registro['CTPS'] = int(input('Carteira de Trabalho (0 se não tiver): '))
if registro['CTPS'] != 0:
    registro['contratação'] = int(input('Ano de contratação: '))
    registro['salário'] = float(input('Salário: R$'))
    registro['aposentadoria'] = registro['contratação'] + 35
print(registro)
for k, v in registro.items():
    print(f'{k} é igual a {v}')
