# -- exercicio 22 - criar um programa que leia o nome completo de uma pessoa e mostre
# • o nome com todas as letras maiúsculas
# • o nome com todas as letras minúsculas
# • quantas letras ao todo (sem considerar espaços)
# • quantas letras tem o primeiro nome

nome = input('Digite o nome completo: ')

primeiro_nome = nome.split()
nome_sem_espacos = nome.replace(' ', '')

print(f'Letras maiúsculas: {nome.upper()}')
print(f'Letras minúsculas: {nome.lower()}')
print(f'Seu nome tem {len(nome_sem_espacos)} letras sem os espaços')
print(f'O seu primeiro nome é {primeiro_nome[0]} e tem {len(primeiro_nome[0])} letras')
