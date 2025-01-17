#Melhore o jogo do DESAFIO 028, onde o computador vai "pensar"  em um número entre 0 e 10. Só que agora, o jogador vai tentar 
# adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint

computador = randint(0, 10)
jogador = None
tentativas = 0

while jogador != computador:
    jogador = int(input('Em que número estou pensando?\n'))
    
    if jogador != computador:
        print('\033[1;31mOpss! Eu não estou pensado nesse número :/\n\033[m')
    tentativas += 1
print(f'\033[1;32mParabéns! Você acertou depois de {tentativas} tentativas.\n\033[m')
