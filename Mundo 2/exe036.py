#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai
#perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor
#da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
from time import sleep

v = float(input('Qual o valor da casa? '))
s = float(input('Qual o salário do comprador? R$ '))
a = int(input('Em quantos anos vai pagar? '))

prestacao = (v/a)

print(f'O valor da prestação é {prestacao:.2f}. Analisando...')
sleep(3)

if (prestacao > (s*0.3)):
    print(f'Empréstimo NEGADO! O valor da prestação é maior que 30% do salário.')
else:
    print('Empréstimo APROVADO!')

