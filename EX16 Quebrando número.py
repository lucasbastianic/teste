#Arredondando número para baixo

from math import floor, trunc

n1 = float(input('Qual o valor do número desejado?'))
print('A porção inteira desse número é {}.'.format(floor(n1)))

#Ou

n1 = float(input('Qual o valor do número desejado?'))
arred = floor(n1)
print('A porção inteira desse número é {}.'.format(arred))

#Ou

n1 = float(input('Qual o valor do número desejado?'))
print('A porção inteira desse número é {}.'.format(trunc(n1)))

#Ou

n1 = float(input('Qual o valor do número desejado?'))
arred = trunc(n1)
print('A porção inteira desse número é {}.'.format(arred))

