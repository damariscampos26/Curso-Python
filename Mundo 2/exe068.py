# Faça um programa que jogue Par ou Ímpar com o computador. O jogo só será interrompido quando o jogador PERDER, mostrando o total
# de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
vitorias = 0

while True:
    print('-'*20); print('JOGO DO PAR OU ÍMPAR'); print('-'*20)
    numero = int(input('Escolha um número: '))
    jogador = str(input('Par ou Ímpar? [P / I]: ')).upper().strip()
    computador = randint(0, 10)

    if 'P' in jogador and (numero + computador) % 2 != 0:
        print(f'Você jogou {numero} e o computador {computador}. Total {numero+computador} DEU ÍMPAR.')
        print(f'FIM DE JOGO! Você ganhou {vitorias} vezes.')
        break
    if 'I' in jogador and (numero + computador) % 2 == 0:
        vitorias += 1
        print(f'Você jogou {numero} e o computador {computador}. Total {numero+computador} DEU PAR.')
        print(f'FIM DE JOGO! Você ganhou {vitorias} vezes.')
        break
    if 'P' in jogador and (numero + computador) % 2 == 0:
        print(f'Você jogou {numero} e o computador {computador}. Total {numero+computador} DEU PAR.')
        print('Você VENCEU!')
        print('Vamos jogar de novo ...')
        vitorias += 1
    elif 'I' in jogador and (numero + computador) % 2 != 0:
        print(f'Você jogou {numero} e o computador {computador}. Total {numero+computador} DEU ÍMPAR.')
        print('Você VENCEU')
        print('Vamos jogar de novo ...')
        vitorias += 1