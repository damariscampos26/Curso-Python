# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.
n = int(input('Digite o número para ver sua tabuada: '))
print('-=-'*14)

for i in range(1, 11):
    print(f'{n} x {i} = {n*i}')
print('-=-'*14)