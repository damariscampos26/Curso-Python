#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi
#o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randrange

n = int(input('Digite qualquer número: '))
escolhido = randrange(6)

if (n == escolhido):
    print(f'Você venceu! Seu número é {n} e meu número também é {escolhido}.')
else:
    print(f'Você perdeu! Eu estava pensando em {escolhido}.')