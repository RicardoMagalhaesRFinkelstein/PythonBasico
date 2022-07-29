#Ler os catetos de um triângulo retângulo e retornar a hipotenusa
import math
catOp = float(input('Digite o comprimento do cateto oposto: '))
catAdj = float(input('Digite o comprimento do cateto adjacente: '))

hipo = math.hypot(catOp, catAdj)

print(f'A hipotenusa vale {hipo:.2f}')

math.