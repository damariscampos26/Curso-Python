#Escreva um programa que leia dois números e compare-os mostrando na tela uma mensagem: "O primeiro valor é maior", "O segundo valor é maior" ou "Não existe valor maior, os dois são 
# iguais".
from time import sleep

number1 = int(input('Digite o primeiro número: '))
number2 = int(input('Digite o segundo número: '))
print('Verificando...')
sleep(1)

if (number1 > number2):
    print('O primeiro valor é maior!')
elif (number2 > number1):
    print('O segundo valor é maior!')
else:
    print('Não existe valor maior, os dois são iguais!')