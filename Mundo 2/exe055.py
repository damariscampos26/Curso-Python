# Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e menor peso lidos.
maior = 0
menor = 0

for contador in range(0, 5):
    peso = float(input('Qual o seu peso? '))

    if contador == 0:
        maior = peso
        menor = peso
    else:
        # maior = ((maior + peso + abs(maior - peso)) / 2)
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'O maior peso é {maior}Kg.')
print(f'O menor peso é {menor} Kg.')