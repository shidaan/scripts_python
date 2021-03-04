# desafio 18 -- ler um ângulo e calcular o cosseno, seno e tangente
from math import sin, cos, tan

angulo = float(input('Digite o ângulo: '))

print(f'{"Seno":.<10}{sin(angulo):.>20,.2f}')
print(f'{"Cosseno":.<10}{cos(angulo):.>20,.2f}')
print(f'{"Tangente":.<10}{tan(angulo):.>20,.2f}')
