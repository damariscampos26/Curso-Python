#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e 
# mostre sua categoria, de acordo com a idade: 1 - até 9 anos: mirim; 2 - até 14 anos: infantil; 
#até 19 anos: júnior, até 20 anos: sênior; acima: master.
from datetime import date

ano = int(input('Qual o seu ano de nascimento? '))
idade = (date.today().year - ano)

if (idade <= 9):
    print('Categoria: MIRIM')
elif (9 < idade <= 14):
    print('Categoria: INFANTIL')
elif (14 < idade <= 19):
    print('Categoria: JÚNIOR')
elif (19 < idade <= 20 ):
    print('Categoria: SÊNIOR')
else:
    print('Categoria: MASTER')