#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar R$7.00 por cada km acima do limite.
v = float(input('Digite a velocidade do carro: '))

if (v > 80):
    multa = (7 * (v - 80))
    print('Você foi MULTADO!')
    print(f'Você irá pagar R$ {multa:.2f} de multa!')
else:
    print('Boa viagem!')