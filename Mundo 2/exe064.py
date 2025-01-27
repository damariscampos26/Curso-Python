# Crie um programa que leia vários números inteiros pelo  teclado. O programa só vai parar quando o usuário digitar o valor 999, 
# que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
numeros = 0
soma = 0
quantidade = 0
numeros = int(input('Digite um número inteiro (999 para sair): '))

while numeros != 999:
    soma += numeros
    quantidade += 1
    numeros = int(input('Digite um número inteiro (999 para sair): '))
print(f'Você digitou {quantidade} números e a soma deles é {soma}.')