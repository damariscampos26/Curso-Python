# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o
# nome dos quatro alunos e mostre a ordem sorteada.
from random import sample, shuffle

a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')

lista = [a1, a2, a3, a4]
shuffle(lista)
# print(f'A ordem de apresentação dos alunos é {sample(lista, k=len(lista))}')
print(f'A ordem de apresentação dos alunos é {lista}')