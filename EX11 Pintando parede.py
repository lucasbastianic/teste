#Calculo de tinta para pintar parede
 
altura = float(input('Qual a altura da parede?'))
largura = float(input('Qual a largura da parede'))
print('Sua parede possui {} m² e para pintar será necessário {} litros de tinta'.format(altura*largura, (altura*largura)/2))

#Ou

altura = float(input('Qual a altura da parede?'))
largura = float(input('Qual a largura da parede'))
m2 = altura * largura
tinta = m2 /2
print('Sua parede possui {} m² e para pintar será necessário {} litros de tinta'.format(m2, tinta))