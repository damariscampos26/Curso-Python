# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e 
# qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
from time import sleep
media = 0
contador = 0
soma = 0
opcao = int(input('\nDigite um número (0 para sair): '))

while opcao != 0:
    soma += opcao
    contador +=1
    opcao = int(input('\nDigite um número (0 para sair): '))
    media = soma / contador

sleep(1)
print('\nVocê saiu do programa!')
sleep(1)
print(f'\nA média dos números digitados é {media}.')