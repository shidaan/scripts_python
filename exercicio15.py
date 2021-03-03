# desafio 15 -- aluguel de carros - R$ 60 dia, R$ 0,15 km
km = float(input('Digite quantos quilômetros foram corridos: '))
dia = int(input('Digite quantos dias o carro foi alugado: '))

aluguel = (dia * 60) + (km * 0.15)

print(f'Referente aos {km}km percorridos e {dia} dias alugados, o aluguel ficou no valor de R$ {aluguel:.2f}')
