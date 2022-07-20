#ler a altura e largura de uma parede, calcular a sua área e descobrir quantos litros de tinta serão necessários, assumindo que cada litro pinte 2m²

altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))

area = largura*altura

print(f'Dado esses valores, a área total da parede é de {area} metros quadrados, e nós precisaremos de {area/2} litros de tinta para pintar tudo.')