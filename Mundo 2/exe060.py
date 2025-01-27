#Faça um programa que leia um número qualquer e mostre seu fatorial.
numero = int(input('Digite um número para ver seu fatorial: '))
cont = numero
fatorial = 1

while cont > 0:
    #fatorial = cont * fatorial
    fatorial = cont * fatorial
    cont -= 1
print(f'{numero}! = {fatorial}')    
