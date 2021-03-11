# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Valor do salário: '))

if salario <= 1250.00:
    reajuste = salario + (salario * 0.15)
else:
    reajuste = salario + (salario * 0.10)

print(f'O R$ {salario} subiu para R$ {reajuste:.2f}')
