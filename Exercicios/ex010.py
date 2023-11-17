# Desafio 010
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

# Saída
print('Este programa é um Conversor de Moedas\n\nConsidere\n\n1 Dólar (EUA) = R$4,90\n')
# Entrada
dolar = float(input('Digite quanto dinheiro você tem na carteira em Real (BRL):\t'))
# Processamento
real = dolar / 4.90
# Saída
print('O dinheiro que você tem na carteira convertido para Dólar (EUA) é:\t{:.2f}'.format(real))
print('BRL R${:.2f} <> USD${:.2f}'.format(dolar, real))

