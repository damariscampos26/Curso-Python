#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
#o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
n = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)
escolhido = randint(0, 5)

if (n == escolhido):
    print(f'PARABÉNS! Eu estava mesmo pensando no número {escolhido}!')
else:
    print(f'GANHEI! Eu estava pensando em {escolhido} e não no {n}.')