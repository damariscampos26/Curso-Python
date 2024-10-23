#Desenvolva um programa que pergunte a distãncia de uma viagem em km. Calcule o preço da passagem, cobrando R$0.50 por km para 
# viagens de até 200km e R$0.45 para viagens mais longas.
distancia = float(input('Qual a distância da viagem? '))

if (distancia <= 200):
    print(f'O valor da passagem é R$ {distancia*0.50:.2f}')
else:
    print(f'O valor da passagem é R$ {distancia*0.45:.2f}')