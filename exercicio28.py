# Exercício Python 28: Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randrange
from time import sleep

print('\033[1;33m:+:\033[m' * 15)
print('   \033[1;36mTente advinhar o número gerado de 0 à 5\033[m')
print('\033[1;33m:+:\033[m' * 15)

# variaveis
num = randrange(0,6)  # gera um número de 0 à 5
user_num = int(input('Digite o número: '))  # o usuário tenta adivinhar o número

print('\033[1;35mPROCESSANDO...\033[m')
sleep(1.25)  # sleep faz o delay para prosseguir com o código

# condição
if user_num == num:
    print(f'\033[1;32mO número gerado foi: {num}. Você venceu!\033[m')
else:
    print(f'\033[1;31mO número gerado foi: {num}. Não foi dessa vez!\033[m')
