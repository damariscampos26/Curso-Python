#Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.
numero = int(input('Digite um número para descobrir se ele é par ou ímpar: '))

if (numero % 2) == 0:
    print(f'{numero} é par!')
else:
    print(f'{numero} é ímpar!')