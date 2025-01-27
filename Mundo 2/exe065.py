# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e 
# qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
from time import sleep
media = 0
quantidade = 0
soma = 0
maior = 0
menor = 0

numero = int(input('\nDigite um número (0 para sair): '))
while numero != 0:
    soma += numero
    quantidade +=1
    if quantidade == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        elif numero < menor:
            menor = numero
    numero = int(input('\nDigite um número (0 para sair): '))

media = soma / quantidade

sleep(1)
print('\nVocê saiu do programa!')
sleep(1)
print(f'\nA média dos números digitados é {media:.2f}. \nO maior número digitado foi {maior}. \nO menor número digitado foi {menor}')
