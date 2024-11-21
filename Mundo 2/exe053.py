# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
frase = str(input('Frase: ').upper().strip())
frase_junto = frase.replace(' ', '')
frase_inverso = ''

for letra in range(len(frase_junto) - 1, -1, -1):
    frase_inverso += frase_junto[letra]

if frase_junto == frase_inverso:
    print(f'A frase {frase_junto} é um palíndromo!')
else:
    print(f'A frase {frase_junto} não é um palíndromo!')