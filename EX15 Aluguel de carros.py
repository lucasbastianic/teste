#Calculo do valor do aluguel de um carro

km = int(input('Quantos KMs você percorreu?'))
dias = int(input('Quantos dias você percorreu?'))
print('Você precisa pagar {} pelo aluguel do carro'.format((dias * 60) + (km * 0.15)))

#Ou

km = int(input('Quantos KMs você percorreu?'))
dias = int(input('Quantos dias você percorreu?'))
valor_km = km * 0.15
valor_dias = dias * 60
total = valor_km + valor_dias
print('Você precisa pagar {} pelo aluguel do carro'.format(total))
