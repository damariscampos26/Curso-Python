# Crie um programa que vai ler vários números e colocar em uma lista. Depois disso,crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas gerados.

numbers =  list()
odd = list()
even = list()

while True:
    numbers.append(int(input("Digite o número para adicioná-lo na lista: ")))

    # Sair do programa 
    while True:
        option = input("Deseja continuar [S / N]: ").upper()

        if option in ['S', 'N']:
            break
    
    if 'N' in option:
        break

# Listas extras com os valores pares e ímpares
for number in numbers:
    if number % 2 == 0:
        even.append(number)
    else:
        if number % 2 != 0:
            odd.append(number)

# Exibindo as listas
print()
print("-" * 25)
print(f"Lista com  todos os números: {numbers}.")
print(f"Lista com os números pares:  {even}.")
print(f"Lista com os números ímpares: {odd}.")