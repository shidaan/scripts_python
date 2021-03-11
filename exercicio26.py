# exercicio26 -- faça um programa que leia uma frase pelo teclado e mostre
# • quantas vezes aparece a letra 'A'
# • em que posição ela aparece pela primeira vez
# • em que posição ela aprece a última vez

frase = str(input('Digite uma frase: ')).strip().upper()

cont = frase.count('A')
primeira_posicao = frase.find('A')
ultima_posicao = frase.rfind('A')

print(f'Na frase tem {cont} letra(s) "A"')
print(f'A letra "A" aparece pela primeira vez na posição {primeira_posicao}')
print(f'A letra "A" aparece pela última vez na posição {ultima_posicao}')
