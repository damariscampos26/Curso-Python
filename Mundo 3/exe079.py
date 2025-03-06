# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre - os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()

# Adiciona os números na lista
while True:
    numero = int(input("Digite o número: "))

    # Verifa se o número já existe na lista
    if numero not in numeros:
        numeros.append(numero)
        print("Número adicionado na lista.")
    else:
        print(f'Número duplicado! Não adicionado na lista.')
            
    # Verifica se o usuário digitou 's' ou 'n'
    while True:
        opcao = input("Deseja continuar? [S / N]: ").lower().strip()
        if opcao in ['s', 'n']:
            break
        else:
            print('Digite uma opção válida!')

    # Se ele digitar 'n', o programa encerra
    if opcao in 'n':
        break

# Exibe os valores em ordem crescente
numeros.sort()
print(f'Números em ordem crescente: {numeros}.')