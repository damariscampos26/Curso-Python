# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de
# 1 até 500.
j = 0
for i in range(1, 501):
    if (i % 3 == 0) and (i % 2 != 0):
        j += i
print(f'A soma de todos os números ímpares e múltiplos de 3 é {j:.2f}')
