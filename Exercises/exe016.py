# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua parte inteira.
from math import trunc

x = float(input('Digite um número real: '))
print(f'A parte inteira do número {x} é {trunc(x)}.')