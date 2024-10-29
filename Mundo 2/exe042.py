#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#1 - Equilátero: todos os lados iguais; 2 - Isósceles: dois lados iguais; 3 - Escaleno: todos os lados 
# diferentes.
a = float(input('Qual o comprimento do lado A? '))
b = float(input('Qual o comprimento do lado B? '))
c = float(input('Qual o comprimento do lado C? '))

if (a == b) and (a == c):
    print('Triângulo Equilátero!')
elif (a == b) or (a == c):
    print('Triângulo Isósceles!')
elif a < (b + c) and b < (a + c) and c < (a + b): 
    print('Triângulo Escaleno!')
else:
    print('Não é possível formar um triângulo!')