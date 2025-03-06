# Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta (sem usar o sort). No final, mostre a lista ordenada.

numbers = []

# Criando a lista com os cinco valores
for counter in range(0, 5):
    number = int(input(f"Digite o número para adicioná-lo à lista: "))

    if counter == 0 or number > numbers[-1]:
        numbers.append(number)
        print("Adicionado ao final da lista.")
    else:
        position = 0

        while position < len(numbers):
            if number <= numbers[position]:
                numbers.insert(position, number)
                print(f"Adicionado na posição {position} da lista.")
                break
            position += 1
print(numbers)