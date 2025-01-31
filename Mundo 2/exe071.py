# Crie um programa que simule o funcionamento de um caixa eletrônico. No incício, pergunte ao usuário qual será o valor a ser sacado
# (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.Considere que o caixa possui cédulas de
# R$50, R$20, R$10 e R$1.
while True:
    print('='*30)
    print('BANCO DE DINHEIRO :D'.center(29))
    print('='*30)
    valor = int(input('Quanto vocẽ vai sacar? '))

    nota50 = valor // 50
    if nota50 > 0:
        print(f'{nota50} notas de R$50')

    nota20 = (valor - (nota50*50)) // 20
    if nota20 > 0:
        print(f'{nota20} notas de R$20')

    nota10 = (valor - (nota50*50) - (nota20*20)) // 10
    if nota10 > 0:
        print(f'{nota10} notas de R$10')

    nota1 = valor - (nota50*50) - (nota20*20) - (nota10*10)
    if nota1 > 0:
        print(f'{nota1} notas de R$1')
    break

