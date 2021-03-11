# exercicio24 -- leia um nome de uma cidade e diga se ela começa ou não com o nome "SANTO"

cidade = str(input('Digite a cidade: ')).strip()

if 'SANTO' in cidade[:5].upper():
    print('A cidade começa com SANTO')
else:
    print('A cidade não começa com SANTO')
    