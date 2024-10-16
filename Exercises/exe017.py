# Faça um programa que leia o comprimento do cateto oposto e cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
from math import hypot

co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
h = hypot(co, ca)

print(f'O comprimento da hipótenusa é: {h:.0f}.')