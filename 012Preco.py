#Ler o preço de um item, calcular qual o desconto de 5% e moostrar o novo preço

preco = float(input('Digite o preço do item: '))
print(f'Com o desconto de 5%, que no caso equivale a {preco*0.05:.2f} reais, o preço final do produto é de {preco*0.95:.2f} reais.')