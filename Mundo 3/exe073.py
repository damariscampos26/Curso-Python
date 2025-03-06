# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. 
# Depois mostre: a)Apenas os 5 primeiros colocados; b)Os últimos 4 colocados da tabela; c)Uma lista com os times em ordem alfabética; 
# d)Em que posição na tabela está o time da Chapecoense.
times = (
         'Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 
         'Internacional', 'São Paulo', 'Corinthians', 'Bahia', 
         'Cruzeiro', 'Vasco da Gama', 'EC Vitória', 'Atlético MG',
         'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 
         'Athletico-PR', 'Criciúma', 'Atlético-GO', 'Cuiabá',
         )
# a)Apenas os 5 primeiros colocados.
print(f'\033[1mOs 5 primeiros colocados:\033[m {times[0:5]}\n')
print('-='*30)

# b)Os últimos 4 colocados da tabela.
print(f'\033[1mOs 4 últimos colocados:\033[m {times[16:]}\n')
print('-='*30)

# c)Uma lista com os times em ordem alfabética.
print(f'Times em ordem Alfabética: {sorted(times)}')
print('-='*30)

# d)Em que posição na tabela está o time da Chapecoense.
if 'Chapecoense' in times:
    posicao_chapecoense = times.index("Chapecoense") + 1 # Somamos 1 ao índice para exibir a posição humana (começando em 1).
    print(f'O time Chapecoense está em {posicao_chapecoense}° lugar.')
else:
    print(f'O time Chapecoense não está na lista!')


