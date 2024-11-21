n = int(input('Digite um número inteiro: '))
total = 0

for i in range(1, n+1):
    if n % i == 0:
        total += 1
if total == 2:
    print(f'{n} é primo!')
else:
    print(f'{n} não é primo!')
