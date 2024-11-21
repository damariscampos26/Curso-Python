# Crie um programa que leia o ano de nascimento de 7 pessoas. No final, mostre quantas pessoas não atingiram a maioridade e quantas
#já são maiores.
from datetime import date

soma1 = 0
soma2 = 0

for contador in range(7):
    ano = int(input('Qual seu ano de nascimento? '))
    idade = date.today().year - ano
    
    if (idade >= 21):
        soma1 += 1
    else:
        soma2 += 1
print(f'{soma1} pessoas já atingiram a maioridade!')
print(f'{soma2} pessoas não atingiram a maioridade!')