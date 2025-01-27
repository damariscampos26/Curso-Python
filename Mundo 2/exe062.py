# Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que
# quer mostrar 0 termos.
primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

contador = 0
termo_atual = primeiro_termo

print('PA = ',end=' ')

while contador < 10:
    print(termo_atual, end='  ')
    termo_atual += razao
    contador += 1

quantidade = None

while quantidade != 0: 
    quantidade = int(input('\nCaso queira adicionar mais termos a PA, digite a quantidade (0 para sair): '))
    
    if quantidade > 0:
        novo_contador = 0
        while novo_contador < quantidade:
            print(termo_atual, end='  ')
            termo_atual += razao
            novo_contador += 1
print('\nVocê saiu do programa!')




    