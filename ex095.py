# jogadores = dict()
# dados = list()
# total = 0
# gols = list()
# while True:
#     jogadores['nome'] = str(input('Qual o nome do jogador? ')).strip()
#     for c in range(0, int(input(f'Quantas partidas {jogadores["nome"]} jogou? '))):
#         gols.append(int(input(f'Quantos gols ele fez na partida {c}º? ')))
#         jogadores['gols'] = gols[:]
#         jogadores['total'] = sum(gols[:])
#     dados.append(jogadores.copy())
#     gols.clear()
#     jogadores.clear()
#     while True:
#         conf = str(input('Quer continuar?[S/N] ')).strip().upper()[0]
#         if conf in 'SN':
#             break
#     print('_' * 30)
#     if conf == 'N':
#         break
# print(dados)
# print(f'{"Nu.":<4}{"Nome":<10}{"gols":>12}{"total":>15}')
# n = 0
# for i in dados:
#     print(f'{n:<4}{i["nome"]:<15}{i["gols"]}{i["total"]:>10}')
#     n += 1
# while True:
#     while True:
#         n = 0
#         lev = int(input('Mostrar levantamento de qual jogador?[999 encerra] '))
#         if lev <= len(dados) or lev == 999:
#             break
#     if lev == 999:
#         break
#     else:
#         print(f'-- Levantamento do jogador {dados[lev]["nome"]} --')
#         for v in dados[lev]['gols']:
#             print(f'   Na partida {n} fez {dados[lev]["gols"][n]}')
#             n += 1
# print('FINALZIZADO')
time = list()
jogador = dict()
partidas = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Qual o nome do jogador? ')).strip()
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'    Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
# No final vai ficar: jogador = {'nome': '', 'gols': '[]', 'total': }
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Digite S ou N.')
    if resp == 'N':
        break
print(jogador)
print('-=' * 30)
print('num.', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? [999 encerra] '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com número {busca}!')
    else:
        print(f' -- Levantamento do jogador {time[busca]["nome"]} --')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
print('-' * 40)
print('PROGRAMA FINALIZADO!')
print('Volte sempre!')
