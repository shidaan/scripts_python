# desafio 001
print('Olá, Mundo!')

# desafio 002
nome = input('Digite seu nome: ')
print(f'Prazer em te conhecer, {nome}!')

# desafio 003
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
