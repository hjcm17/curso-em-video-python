# Desafio 004 Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.
objeto: str = (input('Digite algo: ')) #Entrada
print('Tipo primitivo: ', type(objeto)) # Atribuição de texto string na variável 'tipo'
#Saída
print('Só tem espaços? ', objeto.isspace())
print('Só tem número? ', objeto.isnumeric())
print('É alfabético? ', objeto.isalpha())
print('É alfanumérico? ', objeto.isalnum())
print('Está em maiúsculas? ', objeto.isupper())
print('Está em menúsculas?', objeto.islower())
print('Está capitalizada? ', objeto.istitle())


