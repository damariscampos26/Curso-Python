# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre: a) QUANTOS NÚMEROS FORAM DIGITADOS; b) A LISTA DE VALORES ORDENADA DE FORMA DECRESCENTE; c) SE  O VALOR 5 FOI DIGITADO  E ESTÁ OU NÃO NA LISTA.
numeros = []

while True: 
    numeros.append(int(input("Digite o número: ")))

    while True:
        opcao = input("Deseja continuar? [S / N]: ").upper()
        if opcao in ['S', 'N']:
            break

    if 'N' in opcao:
        break

print("\n-" * 10)

# QUANTIDADE DE NÚMEROS 
print(f"Você digitou {len(numeros)} números!")

# LISTA ORDENADA DE FORMA DESCRESCENTE 
numeros.sort(reverse=True)
print(f"Números em ordem decrescente: {numeros}")

# SE O NÚMEROS 5 ESTÁ NA LISTA
if 5 in numeros:
    print(f"O números 5 está na lista!")
else:
    print("O número 5 não foi encontrado na lista!")