largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))
area = altura*largura
tinta = area/2

print(f'Sua parede tem dimensão de {largura}x{altura} e a área é de {area}m². \nPara pintar a parede, você precisará de {tinta:.1f}L de tinta.')