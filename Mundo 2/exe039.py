#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade: 1 - se ele ainda vai se alistar ao serviço militar; 2 - se é hora de se alistar;
# 3 - se já passou do alistamento. Seu programa também deverá mostrar o tempo que faltou ou que passou do prazo.
from datetime import date

ano = int(input('Qual o seu ano de nascimento? '))
idade = date.today().year - ano

if (idade == 18):
    print(f'Você já tem {idade} anos e DEVE se alistar no Serviço Militar!')
elif (idade <  18):
    tempo = abs(idade - 18)
    print(f'Você tem {idade} anos e faltam {tempo} anos para você se alistar no Serviço Militar!')
else:
    tempo2 = abs(idade - 18)
    print(f'Você tem {idade} anos e passaram {tempo2} anos do prazo de se alistar no Serviço Militar!')