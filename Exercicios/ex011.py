# Desafio 011
# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m²

# Entrada
largura = float(input('Digite a largura (em metros) da parede: '))
altura = float(input('Digite a altura (em metros) da parede: '))

# Processamento
area = largura * altura
tinta = area / 2

# Saída
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².\nVocê irá precisar de {}l de tinta'.format(largura, altura, area, tinta))