# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import cos, sin, tan

a = float(input('Digite o ângulo: '))

print(f'O seno do ângulo {a} é {sin(a)}.')
print(f'O cosseno do ângulo {a} é {cos(a)}.')
print(f'A tangente do ângulo {a} é {tan(a)}.')


