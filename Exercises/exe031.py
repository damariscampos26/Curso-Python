distancia = float(input('Digite a distância da viagem em Km: '))

if (distancia <= 200):
    print(f'O valor da passagem é R$ {distancia*0.50:.2f}')
else:
    print(f'O valor da passagem é R$ {distancia*0.45:.2f}')