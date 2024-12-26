#Verificando quantas pessoa são maiores de 18 anos

from datetime import datetime

ano = datetime.now().year
x = 0 
for i in range (0,7):
    anon = int(input('Qual o ano do seu nascimento'))
    if ano - anon >= 18:
        x += 1
print('{} pessoas já atingiram a maioridade'.format(x))
print('{} pessoas ainda não são maiores'.format(7-x))