#Ler um número e mostrar o seu dobro, triplo e raiz quadrada

numero = float(input('Digite um numero qualquer: '))
print(f'O dobro de {numero:.0f} é {numero*2:.0f}.')
print(f'O triplo de {numero:.0f} é {numero*3:.0f}.')
print(f'A raiz quadrada de {numero:.0f} é {pow(numero,(1/2)):.2f}.') 