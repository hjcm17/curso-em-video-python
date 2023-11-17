# Desafio 008
# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

# Entrada
metros = float(input('Digite o valor do comprimento(em metros):'))
# Processamento
centimetro = metros * 100
milimetro: float = metros * 1000

# Saída
print('O valor {} metros convertido para centímetros é: {} cm\nO valor {} metros convertido para milimetros {} mm'
      .format(metros, centimetro, metros, milimetro))
