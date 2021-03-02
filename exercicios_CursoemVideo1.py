# # desafio 001
# print('Olá, Mundo!')

# # desafio 002
# nome = input('Digite seu nome: ')
# print(f'Prazer em te conhecer, {nome}!')

# # desafio 003
# n1 = int(input('Primeiro número: '))
# n2 = int(input('Segundo número: '))
# print(f'A soma entre {n1} e {n2} é = {n1 + n2}')
# # print('A soma é ', (n1 + n2))

# desafio 4
info = input('Digite algo: ')
print(f'O tipo primitivo desse valor é: {type(info)}')
print(f'Só tem espaços? {info.isspace()}')
print(f'É um número? {info.isnumeric()}')
print(f'É alfabético? {info.isalpha()}')
print(f'É alfanumérico? {info.isalnum()}')
print(f'Está em maiúsculas? {info.isupper()}')
print(f'Está em minúsculas? {info.islower()}')
print(f'Está capitalizada? {info.istitle()}')
