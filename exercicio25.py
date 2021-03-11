# exercicio25 -- ler o nome de uma pessoa e diga se ela tem "SILVA" no nome

nome = str(input('Digite o nome inteiro: ')).strip()

# if nome.upper().find('SILVA'):
if 'SILVA' in nome.upper():
    print('O nome da pessoa tem "SILVA"')
else:
    print('O nome da pessoa não tem "SILVA"')