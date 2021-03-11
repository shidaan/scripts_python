# exercicio 30 - ler um número e mostrar se é par ou ímpar

num = int(input('\033[1;35mDigite um número:\033[m '))

if num % 2 == 0:
    print('O número é \033[1;32mpar\033[m')
else:
    print('O número é \033[1;31mímpar\033[m')
