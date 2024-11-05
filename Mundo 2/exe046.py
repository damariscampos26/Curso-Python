# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa
# de 1s entre eles.
from time import sleep

for c in range(10, 0, -1):
    print(c)
    sleep(1)
for i in range(0,3):   
    fogos = "-`' Pow '´- ¬_¬"
    print (fogos)
    sleep(0.5)
