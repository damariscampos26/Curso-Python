# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os dez primeiros termos dessa progressão
t = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão: '))

for i in range(t, 10*r+t, r):
    print(i, end=' → ')
print('FIM')

