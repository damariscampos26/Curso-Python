#Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
#1 - para binário, 2 - para octal e 3 - para hexadecimal.
from time import sleep

print('-=-'*30)
print('CONVERSOR DE NÚMEROS'.center(80))
print('-=-'*30)
sleep(1)

n = int(input('Digite um número inteiro: '))
o = int(input('Qual será a base de conversão? \n1 - BINÁRIO \n2 - OCTAL \n3 - HEXADECIMAL: '))

if (o == 1):
    print(f'Convertendo o número {n} para binário...')
    sleep(3)
    print(f' O número {n} em binário é {n:b}')
elif(o == 2):
    print(f'Convertendo o número {n} para octal...')
    sleep(3)
    print(f'O número {n} em octal é {n:o}')
elif (o == 3):
    print(f'Convertendo o número {n} para hexadecimal...')
    sleep(3)
    print(f'O número {n} em hexadecimal é {n:x}')
else:
    print('Selecione uma opção válida!')