#Ler um número real qualquer e mostrar na tela apenas a sua porção inteira
import math #também poderia import trunc from math, de modo á importar somente o método  necessário

valor = float(input('Digite um valor: '))

print(f'O valor digitado foi {valor} e a porção inteira dele é {math.trunc(valor)}') #caso eu desse o import mais específico, poderia remover o math. deixando somente o trunc
