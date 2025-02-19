# Desenvolva um programa que leia quatro valores pelo teclado e guarde - os em uma tupla. No final, mostre: a)Quantas vezes apareceu
# o valor 9. b)Em que posição foi digitado o primeiro valor 3. c)Quais foram os números pares.

numeros = (
           int(input('Digite um número: ')), 
           int(input('Digite outro número: ')),
           int(input('Digite um terceiro número: ')),
           int(input('Digite o último número: '))
           )
# Quantas vezes o número 9 aparece
print(f'\nO número 9 aparece {numeros.count(9)} vezes.')

# Posição do número 3
if 3 in numeros:
    print(f'O número 3 aparece na {numeros.index(3)+1}ª posição.')
else:
    print('O número 3 não foi digitado!')

# Números pares
for numero in numeros:
    if numero % 2 == 0:
        print(f'{numero}', end=' ')
print('são pares.')