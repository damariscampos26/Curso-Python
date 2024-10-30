#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep

v = float(input('Qual o valor da casa? R$ '))
s = float(input('Qual o salário do comprador? R$ '))
a = int(input('Em quantos anos vai pagar? '))

prestacao = (v / (a * 12))

print(f'\nO valor da prestação é R$ {prestacao:.2f}')
sleep(3)
print(f'\n30% do seu salário equivale a R$ {s*0.3}')
sleep(3)
print('\nAnalisando Empréstimo...')
sleep(3)

if (prestacao > (s*0.3)):
    print(f'\nEmpréstimo NEGADO! O valor da prestação é maior que 30% do salário.')
else:
    print('\nEmpréstimo APROVADO!')

