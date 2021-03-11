# exercicio 27 -- faça um programa que leia o nome completo de uma pessoa, mostrando em seguida
# o primeiro e o último nome separadamente

nome = str(input('Digite o nome completo: ')).strip()

nome_aux = nome.split()

print(f'Nome: {nome}')
print(f'Primeiro nome: {nome_aux[0]}')
print(f'Último nome: {nome_aux[-1]}')
