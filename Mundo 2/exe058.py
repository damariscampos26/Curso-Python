#Melhore o jogo do DESAFIO 028, onde o computador vai "pensar"  em um número entre 0 e 10. Só que agora, o jogador vai tentar 
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

computador = randint(0, 10)
jogador = None
cont = 0

while jogador != computador:
    jogador = int(input('Em que número estou pensando?\n'))
    cont += 1
print(f'Parabéns! Você acertou depois de {cont} tentativas.')
