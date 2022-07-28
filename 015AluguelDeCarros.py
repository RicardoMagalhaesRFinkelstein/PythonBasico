km = int (input('Quantos quilômetros foram rodados? '))
dias = int(input('Por quantos dias você ficou com o carro? '))
valor = (km*0.5) + (dias * 120)

print(f'O valor á pagar será de R${valor:.2f}')

