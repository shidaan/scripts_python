# desafio 19 -- fazer uma aplicação que sorteia 1 aluno entre 4
from random import choice, randrange

nome1 = input('Aluno 1: ')
nome2 = input('Aluno 2: ')
nome3 = input('Aluno 3: ')
nome4 = input('Aluno 4: ')

lista = [nome1, nome2, nome3, nome4]
x = choice(lista)

print(f'O aluno sorteado foi o {lista[randrange(4)]}')
# ou 
print(f'O aluno sorteado foi o {x}')
