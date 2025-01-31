# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, 
# mostre: a)Qual o total gasto na compra. b)Quantos produtos custam mais de R$1.000. c)Qual é o nome do produto mais barato.
quantidade = custo_total = menor_preco = 0
produto_barato = None

while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$'))
    custo_total += preco
    
    if menor_preco == 0 or preco < menor_preco:
        menor_preco = preco
        produto_barato = produto

    if preco > 1000:
        quantidade += 1
    
    while True:
        opcao = input('Deseja continuar? [S / N] ').upper().strip()

        if opcao in ['S', 'N']:
            break
    if 'N' in opcao:
        break
print(f'\nO custo total da compra foi R${custo_total}. \n{quantidade} produtos custam mais de R$1.000. \nO produto mais barato é {produto_barato}, que custa R${menor_preco}.\n')
print('Programa encerrado.')