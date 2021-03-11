# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = int(input('Qual a velocidade do carro?: '))
print('\n')

if velocidade <= 80:
    print(f'O carro estava à \033[1;32m{velocidade}km\033[m, o qual está no limite permitido')
else:
    multa = (velocidade - 80) * 7
    print(f'O carro estava à \033[1;31m{velocidade}km\033[m, o qual está acima do limite permitido que é 80km')
    print(f'\033[1;31mO carro foi multado...\033[m A multa vai custar R$ 7.00 por cada km excedido que é 80km')
    print(f'Km excedidos: {velocidade-80}km')
    print(f'Total da multa: R$ {multa:.2f}')
    