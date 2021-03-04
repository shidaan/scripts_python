from random import randint

num_comp = randint(1, 100)
break_2 = True
count_erros = 0

while break_2 == True:
    try:
        while True:

            n = int(input('Adivinhe um número de 1 ao 100: '))

            if n < num_comp:
                print('O número é \033[1;36m\u2191\033[m')  # Maior
                count_erros += 1
            elif n > num_comp:
                print('O número é \033[1;36m\u2193\033[m')  # Menor
                count_erros += 1
            elif n == num_comp:
                print(
                    f'\n\033[1;32mParabéns!\033[m \nVocê acertou na \033[1;31m{count_erros}ª\033[m tentativa!')
                break_2 = False
                break

    except ValueError:
        print('Somente números inteiros')
