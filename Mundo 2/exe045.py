from random import choice
from time import sleep

print('-'*20)
print('INICIANDO O JOGO')
print('-'*20)
sleep(2)

jogador = input('Você escolhe pedra, papel ou tesoura? ')
lista = ['pedra', 'papel', 'tesoura']
computador = choice(lista)
print('Analisando...')
sleep(2)

if (jogador == computador):
   print(f'EMPATE! Eu escolhi {computador} e você {jogador} também!')
elif (
    (jogador == 'papel' and computador == 'pedra') or 
    (jogador == 'pedra' and computador == 'tesoura') or 
    (jogador == 'tesoura' and computador == 'papel')
    ):
    print(f'VOCÊ GANHOU! Eu escolhi {computador} e você {jogador}.')
else:
    print(f'EU GANHEI! :P \nVocê escolheu {jogador} e eu escolhi {computador}.')

