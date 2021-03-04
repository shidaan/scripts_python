from math import sqrt
import random

num = int(input('Digite um número: '))
aleatorio = random.randint(1,10)  # gera um número aleatório entre 1 e 10

print(f'Raiz Quadrada {sqrt(num):.>20,.2f}')
print(f'Random {aleatorio}')
