#Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC e mostre seu status, de 
#acordo com a tabela abaixo: 1 - abaixo de 18.5: abaixo do peso; entre 18.5 e 25: peso ideal; 25 até 30: 
#sobrepeso; 30 até 40: obesidade; acima de 40: obesidade mórbida.

altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

imc = (peso / (altura ** 2))

if (imc < 18.5):
    print(f'Seu IMC é {imc:.1f} e você está ABAIXO DO PESO!')
elif (18.5 <= imc < 25):
    print(f'Seu IMC é {imc:.1f} e você está com o PESO IDEAL!')
elif (25 <= imc < 30):
    print(f'Seu IMC é {imc:.1f} e você está com SOBREPESO!')
elif (30 <= imc < 40):
    print(f'Seu IMC é {imc:.1f} e você está com OBESIDADE!')
else:
    print(f'Seu IMC é {imc:.1f} e você está com OBESIDADE MÓRBIDA!')