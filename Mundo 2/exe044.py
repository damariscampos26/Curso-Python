#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e 
#condição de pagamento: 1 - à vista (dinheiro, cheque ou pix): 10% de desconto; à vista no cartão: 5% de 
#desconto; em até 2x no cartão: preço normal; 3x ou mais no cartão: 20% de juros.
from time import sleep

print('-'*30) 
print('Condições de pagamento'.center(30))
print('-'*30)

preco = float(input('Qual o valor do produto? R$ '))

print("""\nSelecione uma forma de pagamento:
      \n[1] - À VISTA (DINHEIRO, CHEQUE OU PIX)
      \n[2] - À VISTA NO CARTÃO DE CRÉDITO
      \n[3] - ATÉ 2x NO CARTÃO
      \n[4] - 3x OU MAIS""")
opcao = int(input('\nSUA OPÇÃO: '))

print('\nAguarde um momento...')
sleep(3)

if (opcao == 1):
    desconto = preco - (preco * 0.10)
    print(f'\nVocê selecionou "Pagamento à vista" e ganhou um desconto de 10%. O produto custava R${preco:.2f} e sairá por R${desconto:.2f}!')
elif (opcao == 2):
    desconto = preco - (preco * 0.05)
    print(f'\nVocê selecionou "Pagamento à vista no cartão" e ganhou um desconto de 5%. O produto custava R${preco:.2f} e sairá por R${desconto:.2f}!')
elif (opcao == 3):
    total = (preco / 2)
    print(f'\nVocê parcelou sua compra em 2 vezes de R${total:.2f} e a compra final sairá por R${preco:2f}!')
elif (opcao == 4):
    parcela = int(input('\nEm quantas vezes você quer parcelar? '))
    sleep(3)
    taxa = preco + (preco*0.20)
    total = (taxa / parcela)
    print(f'\nVocê parcelou sua compra em {parcela} vezes de R$ {total:.2f} e teve um aumento de 20%. O produto custava R$ {preco:.2f} e sairá por R${taxa:.2f}')
else:
    print('\nSelecione uma opção válida!')