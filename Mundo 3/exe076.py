# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma 
# listagem de preços, organizando os dados em forma tabular.

print('\033[1;35m-'*40)
print(f'|          LISTAGEM DE PREÇOS          |\033[m'.center(40))
print('\033[1;35m-\033[m'*40)

# Tupla com os produtos
produtos = ('Arroz', 5.69, 'Feijão', 8.82, 'Farinha', 10.90, 'Azeite', 49.56, 'Óleo', 6.36)

# Dados tabulados
for produto in range(0, len(produtos), 2):
    descricao = produtos[produto]
    preco = produtos[produto + 1]
    print(f'{descricao.ljust(31, "-")}  R${preco}')  

print('-'*40)
