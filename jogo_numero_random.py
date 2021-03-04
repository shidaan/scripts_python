import random as r

num_comp = r.randint(1,100)

try:
    while True:    

        n = int(input('Adivinhe um número de 1 ao 100: '))
        print(num_comp)


        if n < num_comp:
            print('O número é \u2191')
        elif n > num_comp:
            print('O número é \u2193')
        elif n == num_comp:
            print('Parabéns')
            break 
        
except ValueError:
        print('Somente números inteiros')