# desafio 20 -- sortear a ordem de apresentação de trabalhos

from random import sample, shuffle

nome1 = input('Aluno 1: ')
nome2 = input('Aluno 2: ')
nome3 = input('Aluno 3: ')
nome4 = input('Aluno 4: ')

lista = [nome1, nome2, nome3, nome4]

print(f'A ordem da apresentação será: {sample(lista, k=4)}')
# ou
shuffle(lista)
print(f'A ordem da apresentação será: {lista}')
