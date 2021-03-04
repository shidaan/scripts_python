# desafio 17 - calcular hipotenusa de um triângulo retângulo
# fórmula - a² + b² = c² | c =  raiz(c)
from math import hypot

a = int(input('Cateto oposto: '))
b = int(input('Cateto adjacente: '))

c = hypot(a,b)

print(f'Hipotenusa: {c}')
