# exercicio 32 - ano bisexto 

from datetime import date

ano = int(input('Digite o ano ou digite 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year  # da biblioteca date, chama o método today() apontando o valor para ano 'date.today().year'

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
