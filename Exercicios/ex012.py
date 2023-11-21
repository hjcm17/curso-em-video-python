# Desafio 012
# Faça um algoritmo que leia o preço de um produto e mostre seu preço, com 5% de desconto.

# Entrada
desconto = 5
produto = float(input('Informe o preço do produto: R$'))

# Processamento
formula_desconto = (produto * desconto) / 100
valor_final = produto - formula_desconto

# Saída
print('O preço do produto R${:.2f} com {}% (R${:.2f}) de desconto vai custar: R${:.2f}'.format(produto, desconto, formula_desconto, valor_final))
