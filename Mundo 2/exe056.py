# Desenvolva um programa que leia o nome, a idade e o sexo de 4 pessoas. No final, mostre a média de idade do grupo e o  nome do homem mais velho.

media = 0
x = None
for contador in range(1, 5):
    print(f'----- {contador}ª PESSOA -----')
    nome = str(input('NOME: '))
    idade = int(input('IDADE: '))
    sexo = str(input('Sexo [M / F]: ')).strip()

    media += idade / 4

    if sexo in 'Mm':
        if x is None:
            x = idade
        if idade >= x:
            x = idade
            mais_velho = nome 

print(f'O nome do homem mais velho é {mais_velho} e ele tem {x} anos.')
print(f'A média das idades é {media} anos.')

