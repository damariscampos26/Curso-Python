#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a digitação novamente
#até ter um valor correto.
sexo = None

while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M / F]: ')).strip().upper()
    
    if sexo != 'M' and sexo != 'F':
        print('\n\033[1;31mDigite uma opção válida!\n\033[m')
print(f'\n\033[1;32mVocê digitou a opção {sexo}.\n')