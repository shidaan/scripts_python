# Exercício Python 31: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

print('\033[33m-=-\033[m' * 12)
print('Até 200km, passagem = R$ 0.50')
print('Acima de 200km, passagem = R$ 0.45')
print('\033[33m-=-\033[m' * 12)

km = float(input('Qual a distância?: '))

if km <= 200.0:
    print(f'A passagem para distância de {km}km vai custar: \033[34mR$ {(km * 0.50):.2f}\033[m')
else:
    print(f'A passagem para distância de {km}km vai custar: \033[34mR$ {(km * 0.45):.2f}\033[m')
