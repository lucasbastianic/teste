#Seno cosseno e tangente de um angulo

from math import sin, cos, tan, radians
ang = int(input('Qual o angulo?'))
seno = sin(radians(ang))
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'.format(seno,cosseno,tangente))

#Ou

from math import sin, cos, tan, radians
ang = int(input('Qual o angulo?'))
print('O seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}'. format(sin(radians(ang)), cos(radians(ang)),tan(radians(ang))))