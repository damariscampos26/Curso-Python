# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
from time import sleep

print('=-='*20)
print('Analisador de Triângulos'.center(60))
print('=-='*20)

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))

print('Analisando...')
sleep(3)

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('É possível formar um triângulo!')
else: 
    print('Não é possível formar um triângulo!')