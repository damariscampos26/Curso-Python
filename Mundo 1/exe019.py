# Um professor quer sortear um dos seus quatros alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo o nome do escolhido.
from random import choice
a1 = input('Digite o nome do aluno 1: ')
a2 = input('Digite o nome do aluno 2: ')
a3 = input('Digite o nome do aluno 3: ')
a4 = input('Digite o nome do aluno 4: ')

lista = [a1, a2, a3, a4]
aleatorio = choice(lista)
print(f'O aluno sorteado foi {aleatorio}.')