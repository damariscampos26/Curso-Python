# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura 
# while.

primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))

contador = 0
pa = primeiro_termo

while contador < 10:
    print(f'{pa}', end='  ')
    pa += razao
    contador += 1
    
