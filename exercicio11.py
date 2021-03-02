# desafio 11 -- calcular área de uma parede e quantos litros necessários para pintá-la
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
print(f'A parede com dimensões de {larg}mx{alt}m tem área de: {larg*alt}m')
print(f'Serão necessários {(larg*alt)/2}l para pintar a parede')
