# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

numeros = []
maior = menor = 0

for contador in range(0, 5):
    numeros.append(int(input(f"Digite um número para a posição{[contador]}: ")))

    # Identificando o valor maior e menor
    if contador == 0:
        maior = menor = numeros[contador]
    else:
        if numeros[contador] > maior:
            maior = numeros[contador]
        if numeros[contador] < menor:
            menor = numeros[contador]

# Mostrando as posições e o valor maior
print(f'\nO maior número encontrado foi {maior}, na posição ', end=' ')
for indice, valor in enumerate(numeros):
    if valor == maior:
        print(f"{indice}. . .", end=' ')

print()

# Mostrando as posições e o valor menor
print(f'O menor número encontrado foi {menor} na posição ', end=" ")
for indice, valor in enumerate(numeros):
    if valor == menor:
        print(f"{indice}. . .", end=" ")
print()
