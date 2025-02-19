# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler
# um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 
    'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 
    'doze', 'treze', 'quatorze','quinze', 'dezesseis', 
    'dezessete', 'dezoito', 'dezenove', 'vinte'
    )
while True:
    numero = int(input('\n\033[1mDigite um número entre 0 e 20:\033[m '))
    if 0 <= numero <= 20:
        print(f'\nVocê digitou o número \033[1;32m{numeros_extenso[numero]}.\033[m')
        break
    else:
        print('\n\033[1;31mTente novamente!\033[m\n', end='  ')