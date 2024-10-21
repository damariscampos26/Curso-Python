v = float(input('Digite a velocidade do carro: '))

if (v > 80):
    multa = (7 * (v - 80))
    print('Você foi MULTADO!')
    print(f'Você irá pagar R$ {multa:.2f} de multa!')
else:
    print('Boa viagem!')