# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário
# quer ou não continuar. No final, mostre: a)quantas pessoas têm mais de 18 anos. b)quantos homens foram cadastrados. c)quantas 
# mulheres tem menos de 20 anos.
total = mulheres = homens = 0

while True:
    print('-'*23); print('CADASTRE UMA PESSOA'); print('-'*23)
    idade = int(input('Qual a idade? '))

    while True:
        sexo =  input('\nQual o sexo? [F / M] ').upper().strip()
        if sexo in ['F', 'M']:  
            break
    while True:
        opcao = input('\nDeseja continuar? [S / N] ').upper().strip()
        if opcao in ['S', 'N']:
            break
    
    if 'M' in sexo:
        homens += 1
    if idade > 18:
        total += 1
    if 'F' in sexo:
        if idade < 20:
            mulheres += 1
    if 'N' in opcao:
        print(f'\nHá {total} pessoas com mais de 18 anos. \n{homens} homens foram cadastrados. \n{mulheres} mulheres têm menos de 20 anos.')
        print('\nPROGRAMA ENCERRADO!')
        break
        
        