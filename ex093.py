dados = dict()
total = 0
gols = list()
dados['nome'] = str(input('Qual o nome do jogador? ')).strip()
for c in range(1, int(input(f'Quantas partidas {dados["nome"]} jogou? ')) + 1):
    gols.append(int(input(f'Quantos gols ele fez na partida {c}º? ')))
    dados['gols'] = gols[:]
dados['total'] = sum(gols)
print(dados)
print('=-' * 20)
print(f'O jogdaor {dados["nome"]} jogou {len(gols)} partidas:')
for c in range(1, len(gols) + 1):
    print(f'  => Na partida {c}º fez {gols[c - 1]} gols')
print(f'Foi um total de {dados["total"]} gols.')
