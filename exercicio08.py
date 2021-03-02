# desafio 08 -- converter metro em cm e milimitros
metros = float(input('Digite quantos METROS deseja converter: '))
# km hm dam m dm cm mm
print(f'Quilômetros de {metros}m são {metros/1000}km.')
print(f'Hectômetros de {metros}m são {metros/100}hm.')
print(f'Decâmetros de {metros}m são {metros/10}dam')
print(f'Decímetros de {metros}m são {metros*10:.0f}dm')
print(f'Centímetros de {metros}m são {metros*100:.0f}cm')
print(f'Milímetros de {metros}m são {metros*1000:.0f}mm')
