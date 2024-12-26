#Dobro, triplo e raiz de um número
 
n1 = int(input('Digite um número'))
print('Analisando o número {}, o dobro é {}, o triplo é {} e a raiz quadrada é {:.2}'.format(n1, n1*2, n1*3, n1**(1/2)))

#Ou 

n1 = int(input('Digite um número'))
dobro = n1 * 2
triplo = n1 * 3
raiz = n1**(1/2)
print('Analisando o número {}, o dobro é {}, o triplo é {} e a raiz quadrada é {:.2}'.format(n1, dobro, triplo, raiz))