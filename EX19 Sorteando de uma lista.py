#Sorteando um item da lista 

from random import choice

al1 = str(input('Qual o nome do aluno 1?'))
al2 = str(input('Qual o nome do aluno 2?'))
al3 = str(input('Qual o nome do aluno 3'))
al4 = str(input('Qual o nome do aluno 4?'))

lista = [al1,al2,al3,al4]
sort = choice(lista)

print('O aluno sorteado foi {}'.format(sort))
