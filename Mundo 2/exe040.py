#Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem final, de acordo com a média atingida:
#-Média abaixo de 5: REPROVADO. Média entre 5 e 6.9: RECUPERAÇÃO. Média acima 7 ou superior: APROVADO.
nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))

media = ((nota1 + nota2) / 2)

if (media < 5):
    print(f'REPROVADO! Sua média foi {media:.1f}')
elif (5 <= media < 6.9):
    print(f'RECUPERAÇÃO! Sua média foi {media:.1f}')
else:
    print(f'APROVADO! Sua média foi {media:.1f}.')