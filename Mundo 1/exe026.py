frase = input('Digite a frase: ').upper().strip()
print(f'A letra "a" aparece {frase.count('A')} vezes')
print(f'Aparece a primeira vez na posição {frase.find('A')}.')
print(f'Aparece a última vez na posiçao {frase.rfind('A')}.')