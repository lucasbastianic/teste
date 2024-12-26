#Sorteando um item da lista 

from random import shuffle

al1 = str(input('Qual o nome do aluno 1?'))
al2 = str(input('Qual o nome do aluno 2?'))
al3 = str(input('Qual o nome do aluno 3?'))
al4 = str(input('Qual o nome do aluno 4?'))

lista = [al1,al2,al3,al4]
shuffle(lista)

print('A nova ordem será {}'.format(lista))