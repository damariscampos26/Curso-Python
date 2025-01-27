# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma sequencia fibonacci.
quantidade = int(input('Quantos termos da sequencia fibonacci você deseja ver? '))
contador = 0
x = 0
termo1 = 0
termo2 = 1

print(f'Fibonacci = {termo1} → {termo2}', end='')

while contador < quantidade - 2:
    termo3 = termo1 + termo2
    print(end=' → 'f'{termo3}')
    termo1 = termo2
    termo2 = termo3 
    contador += 1