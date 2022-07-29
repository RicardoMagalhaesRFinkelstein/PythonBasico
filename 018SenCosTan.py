#Ler um ângulo qualquer e mostrar o seno, cosseno e tangente desse ângulo

import math
angulo = float(input('Digite o ângulo desejado: '))
angulo = math.radians(angulo)
print(f'O SENO vale {math.sin(angulo):.2f}\nO COSSENO vale {math.cos(angulo):.2f}\nPor fim, a TANGENTE vale {math.tan(angulo):.2f}')

