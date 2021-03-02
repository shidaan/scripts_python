# desafio 12 -- ler um valor e dar 5% de desconto e mostrar na tela
preco = float(input('Preço do produto: R$ '))
desconto = preco - (preco * 0.05)
print(f'O produto de R$ {preco:.2f} com desconto de 5%(R$ {preco * 0.05:.2f}) ficou {desconto:.2f}')
