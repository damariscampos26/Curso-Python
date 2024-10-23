#Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.
from time import sleep
a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segundo número: '))
c = int(input('Digite o terceiro número: '))

print('Verificando quem é o maior e o menor número...')
sleep(3)
#Verifica quem é menor
menor = a
if (b<a and b<c):
    menor = b
if (c<a and c<b):
    menor = c

#Verifica quem é maior
maior = a
if (b>a and b>c):
    maior = b
if (c>a and c>b):
    maior = c

print(f'O maior número é {maior} e o menor é {menor}!')
