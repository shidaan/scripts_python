frase = 'Curso em Vídeo Python'

# fatiamento
print(frase[3])  # pega a string na posição 3 = 's'
print(frase[3:12])  # inicia na posição três e vai até a posição 11 (sempre remove o último valor)
print(frase[:13])  # inicia na posição 0 e vai até a posição 12 (sempre remove o último valor)
print(frase[13:])  # inicia na posição 13 e vai até o final da lista
print(frase[1:15:2])  # inicia na posição 1 e vai até a posição 14 pulando de 2 em 2 casas
print(frase[1::2])  # inicia na posição 1 e vai até o ifnal da lista pulando de 2 em 2 casas
print(frase[::3])  # inicia na posição 0 e vai até o final da lista pulando de 3 em 3 casas

print('''Welcome! Are you completly new to programming?
about why and hou to get started with Python. Fortunately
an experienced programmer in any programming language
(whatever it may be) can pick up Python very quickly.
Its also east for beginners to use and learn, so jump in!
''') #  imprimir uma frase longa em um único print

# cadeia de carcteres
print(frase.count('o'))  # conta os 'o' na lista
print(frase.upper().count('o'))  # upper().count('o') irá contar todos os 'o' maiúsculos na lista 
print(len(frase.strip()))  # strip remove os espaços no começo da lista e no final
print(frase.replace('Python','Android'))  # replace irá substituir nesta instância a palavra Python por Android
print('Curso' in frase)
print(frase.find('Vídeo'))  # irá retornar o valor do lugar onde começou a palavra
print(frase.find('video'))  # como o python tem case sensitive, irá retornar o valor -1
print(frase.lower().find('Vídeo'))  # o lower() irá transformar o find('Vídeo') em minúsculas e procurar na frase
print(frase.capitalize())  # capitalize irá dar upper na primeira letra e lower nas demais letras da frase
print(frase.title())  # title irá transformar todas as letras das primeiras palavras em upper
print(frase.split())  # irá dividir a frase em uma lista com as palavras pertencentes à frase
