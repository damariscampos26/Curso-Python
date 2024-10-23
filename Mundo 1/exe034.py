#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1.250,
#calcule um aumento de 10%. Para inferiores ou iguais, o aumento é de 15%. 
salario = float(input('Qual o seu salárioatualmente? '))

if salario > 1250:
    aumento = salario + (salario * 0.10)
    print(f'Você teve um aumento de 10% e seu salário subiu para {aumento:.2f}')
else:
    aumento = salario + (salario * 0.15)
    print(f'Você teve um aumento de 15% e seu salário subiu para {aumento:.2f}')