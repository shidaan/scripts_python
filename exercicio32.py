# exercicio 32 - ano bisexto 

ano = int(input('Digite o ano: '))

if ano % 100 == 0 and (ano / 100) % 4 == 0:
    print(f'O ano \033[1;32m{ano}\033[m é Bissexto!')
elif ano % 100 != 0 and ano % 4 == 0:
    print(f'O ano \033[1;32m{ano}\033[m é Bissexto!')
else:
    print(f'O ano \033[1;31m{ano}\033[m não é Bissexto!')

# jeito simplificado
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano \033[1;32m{ano}\033[m é Bissexto!')
else:
    print(f'O ano \033[1;31m{ano}\033[m não é Bissexto!')