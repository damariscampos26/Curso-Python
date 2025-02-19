# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados
# e também indique o menor e maior valor que estão na tupla.
from random import randint

# Sorteia 5 números aleatórios.
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

# Mostra os números sorteados e os valores menores e maiores.
print('Os números sorteados foram: ', end='')
for numero in numeros:
    print(numero, end=' ')
print(f'\nO maior número sorteado foi: {max(numeros)}')
print(f'O menor número sorteado foi: {min(numeros)}')