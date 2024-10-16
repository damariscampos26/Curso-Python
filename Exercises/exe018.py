# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import cos, sin, tan, radians

a = float(input('Digite o ângulo: '))
ar = radians(a)

print(f'O seno do ângulo {a} é {sin(ar):.2f}.')
print(f'O cosseno do ângulo {a} é {cos(ar):.2f}.')
print(f'A tangente do ângulo {a} é {tan(ar):.2f}.')


