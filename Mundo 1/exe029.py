#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7.00 por cada km acima do limite.
v = float(input('Digite a velocidade do carro: '))

if (v > 80):
    multa = (7 * (v - 80))
    print('MULTADO! Você excedeu o limite permitido de até 80km/h')
    print(f'Você irá pagar uma multa de R$ {multa:.2f}!')
else:
    print('Boa viagem!')
print('Dirija com segurança!')