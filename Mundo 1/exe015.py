dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos Km percorridos? '))
total_a_pagar = (dias * 60) + (km * 0.15)

print(f'O total a pagar é R${total_a_pagar:.2f}.')