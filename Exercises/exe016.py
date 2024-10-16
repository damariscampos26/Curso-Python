# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua parte inteira.
from math import floor

x = float(input('Digite um número real: '))
print(f'A parte inteira do número {x:.2f} é {floor(x)}.')