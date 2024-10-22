#Faça um programa que leia 3 números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

if (n2 < n1 > n3):
    print(f'{n1} é maior que {n2} e {n3}.')
elif (n1 < n2 > n3):
    print(f'{n2} é maior que {n1} e {n3}.')
else:
    print(f'{n3} é maior que {n1} e {n2}.')
    