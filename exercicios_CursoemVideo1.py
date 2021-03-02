import math

# # desafio 001
# print('Olá, Mundo!')

# # desafio 002 -- imprimir seu nome de forma formatada na tela
# nome = input('Digite seu nome: ')
# print(f'Prazer em te conhecer, {nome}!')

# # desafio 003 -- soma entre 2 valores
# n1 = int(input('Primeiro número: '))
# n2 = int(input('Segundo número: '))
# print(f'A soma entre {n1} e {n2} é = {n1 + n2}')
# # print('A soma é ', (n1 + n2))

# desafio 4 -- disecando variável
# info = input('Digite algo: ')
# print(f'O tipo primitivo desse valor é: {type(info)}')
# print(f'Só tem espaços? {info.isspace()}')
# print(f'É um número? {info.isnumeric()}')
# print(f'É alfabético? {info.isalpha()}')
# print(f'É alfanumérico? {info.isalnum()}')
# print(f'Está em maiúsculas? {info.isupper()}')
# print(f'Está em minúsculas? {info.islower()}')
# print(f'Está capitalizada? {info.istitle()}')

# # desafio 5 -- sucessor e antecessor
# n = int(input('Digite um número: '))
# print(f'Seu antecessor é {n - 1} e seu sucessor é {n + 1}!')

# # desafio 6 -- dobro, triplo e raiz quadrada
# n = int(input('Digite um número: '))
# print(f'Dobro: {n * 2} \nTriplo: {n * 3 }\nRaiz Quadrada: {n ** 0.5}')
# # pode-se usar o math.sqrt(n) para achar a raiz quadrada também

# # desafio 7 -- média de 2 notas
# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# print(f'A média da nota {n1} e {n2} = {(n1 + n2) / 2:.2f}')
# # :.2f formatando a saída para 2 casas decimais depois da virgula

# desafio 8 -- converter metro em cm e milimitros
# m = int(input('Digite quantos METROS deseja converter: '))
# print(f'Centímetros de {m}m: {m * 100} centímetros \nMilímetros de {m}m: {m * 1000} milímetros')

# desafio 9 -- tabuada
# t = int(input('Digite o número que quer a tabuada: '))
# print(f'{t} x 0 = {t*0}')
# print(f'{t} x 1 = {t*1}')
# print(f'{t} x 2 = {t*2}')
# print(f'{t} x 3 = {t*3}')
# print(f'{t} x 4 = {t*4}')
# print(f'{t} x 5 = {t*5}')
# print(f'{t} x 6 = {t*6}')
# print(f'{t} x 7 = {t*7}')
# print(f'{t} x 8 = {t*8}')
# print(f'{t} x 9 = {t*9}')
# print(f'{t} x 10 = {t*10}')

# # desafio 10 -- converter real em dolar
# dolar = 3.27
# real = float(input('Quantos reais você tem? '))
# print(f'Você conseguiu comprar com {real} - {int(real/dolar)} dolar(s)')

# # desafio 11 -- ler área de uma parede e quantos litros necessários para pintar
# # sabendo que 1 litro pinta 2m²
# l = float(input('Largura da parede: '))
# a = float(input('Altura da parede: '))
# a = (l * a) / 2 
# print(f'Você vai precisar de {a:.2f} litros de tinta para pintar essa parede')

# # desafio 12 -- ler um valor e dar 5% de desconto e mostrar na tela
# p = float(input('Preço do produto: '))
# d = p - (p * 0.05)
# print(f'O valor de R$ {p:.2f} com desconto de 5%(R$ {p * 0.05:.2f}) ficou R$ {d:.2f}')

# # desafio 13 -- ler um salário e dar 15% de aumento
# s = float(input('Qual seu salário?: '))
# print(f'Seu salário de R$ {s:.2f} subiu para R$ {s + (s * 0.15):.2f}')
