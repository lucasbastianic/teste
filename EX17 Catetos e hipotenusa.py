#Calculando hipootenusa

op = float(input('Qual o cateto oposto?'))
ad = float(input('Qual o cateto adjacente?'))
print('A hipotenusa desse triangulo é {:.2f}'.format((op ** 2 + ad ** 2) ** (1/2)))

#Ou 

op = float(input('Qual o cateto oposto?'))
ad = float(input('Qual o cateto adjacente?'))
hip = (op ** 2 + ad ** 2) ** (1/2)
print('A hipotenusa desse triangulo é {:.2f}'.format(hip))

#Ou

from math import hypot

op = float(input('Qual o cateto oposto?'))
ad = float(input('Qual o cateto adjacente?'))
print('A hipotenusa desse triangulo é {:.2f}'.format(hypot(op,ad)))

#Ou 

from math import hypot

op = float(input('Qual o cateto oposto?'))
ad = float(input('Qual o cateto adjacente?'))
hip = hypot(op, ad)
print('A hipotenusa desse triangulo é {:.2f}'.format(hip))