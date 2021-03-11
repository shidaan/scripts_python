# exercicio 23 -- faça um programa que leia um número de 0 a 9999 e maostre na tela
# cada um dos digitos separados

num = int(input('Digite um número de 0 a 9999: '))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

# resolução em numera
print(f'unidade: {unidade}')
print(f'dezena: {dezena}')
print(f'centena: {centena}')
print(f'milhar: {milhar}')