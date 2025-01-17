#Crie um programa que leia dois valores e mostre um menu na tela: [1] somar, [2] multiplicar, [3] maior, [4] novos números, [5] sair
#programa. Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
numero1 = int(input('Digite o primeiro número para escolher uma opção no Menu: '))
numero2 = int(input('Digite o segundo número para escolher uma opção no Menu: '))

opcao = 0
while opcao != 5:
    sleep(3)
    print ('\033[1;33m---------- MENU ----------\033[m')
    opcao = int(input('Escolha uma opção:\n'
                      "[1] - Somar\n"
                      "[2] - Multiplicar\n"
                      "[3] - Maior\n"
                      "[4] - Novos números\n"
                      "[5] - Sair\n"
                      "SUA OPÇÃO: "))
    
    if opcao == 1:
        print('Você escolheu a opção SOMAR!')
        print(f'A soma de {numero1} + {numero2} é {numero1 + numero2}.')

    elif opcao == 2:
        print('Você escolheu a opção MULTIPLICAR!')
        print(f'A multiplicação de {numero1} x {numero2} é {numero1 * numero2}.')

    elif opcao == 3:
        print('Você escolheu a opção MAIOR!')
        print(f'O maior número de {numero1} e {numero2} é {(numero1 + numero2 + abs(numero1 - numero2)) / 2:.0f}.')

        print('Você escolheu a opção NOVOS NÚMEROS!')
        numero1 = int(input('Digite o primeiro novo número: '))
        numero2 = int(input('Digite o segundo novo número: '))
        print(f'Você adicionou novos números: {numero1} e {numero2}.')

    elif opcao == 5:
        sleep(3)
        print('Você escolheu a opção SAIR! \nAté mais!')
        
    else:
        print('Escolha uma opção válida!')



    
    