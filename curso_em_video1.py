# print('Olá, Mundo')

# print('\n')

# print(7+4)

# print('\n')

# print('7' + '4')

# print('\n')

# nome  = 'Daniel'
# idade = 23
# peso = 113.5

# print(nome, idade, peso)

# print('\n')

# # nome = input('Qual é seu nome?: ')
# # idade = input('Qual é sua idade?: ')
# # peso = input('Quanto você pesa?: ')

# # print(nome, idade, peso)

# # print('\n')

# # desafio 1 ------------------------------
# nome = input('Qual é o seu nome?: ')
# print('Oká ' + nome + '! Prazer em te conhecer!')

# # desafio 2 ------------------------------
# dia = input('Dia = ')
# mes = input('Mês = ')
# ano = input('Ano = ')
# print('Você nasceu no dia ' + dia + ' de ' + mes + ' de ' + ano + '. Correto?')

# desafio 3 ------------------------------
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
print(f'A soma entre {n1} e {n2} é = {n1 + n2}')
# print('A soma é ', (n1 + n2))

# desafio 4
info = input('Digite algo: ')
print(type(info))

if info.isalnum():
    print(f'{info} é alpha ou numérico')
    if info.isupper():
        print(f'{info} está todo em maiusculo')
    else:
        print(f'{info} está todo em minusculo')
else:
    print(f'{info} não é alpha nem numérico')
