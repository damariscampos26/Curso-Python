#Crie um programa que faça o computador jogar jokenpô com você.
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

if (
    (jogador == 'pedra' and computador == 'tesoura') or
    (jogador == 'papel' and computador == 'pedra') or  
    (jogador == 'tesoura' and computador == 'papel')
    ):
    print(f'VOCÊ GANHOU! Eu escolhi {computador}.')
elif (jogador == computador):
    print(f'EMPATAMOS! Eu escolhi {computador} e você também!')
else:
    print(f'EU GANHEI! :P \nEu escolhi {computador}.')

