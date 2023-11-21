# Desafio 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

# Entrada
aumento = 15
salario = float(input('Informe o salário do funcionário: R$'))

# Processamento
formula_aumento = (salario * aumento) / 100
salario_final = salario + formula_aumento

# Saída
print('Seu salário de R${} com o aumento de {}% (R${:.2f}) é: R${:.2f}'.format(salario, aumento, formula_aumento, salario_final))