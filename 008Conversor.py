#Ler um valor em metros e convertê-lo para centímetros, milímetros e quilômetros

valor = float(input('Digite um valor em metros: '))

print(f'{valor} equivale a {valor*100} centímetros, {valor*1000} milímetros e {valor/1000} quilômetros.')